from textwrap import dedent

from jupyterhub.app import JupyterHub
from jupyterhub.auth import Authenticator
from jupyterhub.handlers import BaseHandler
from jupyterhub.utils import url_path_join
from tornado import gen
from tornado.web import HTTPError
from traitlets.config import Dict, Unicode

from ltiauthenticator.lti11.handlers import LTI11ConfigHandler as LTIConfigHandler
#from ltiauthenticator.lti11.handlers import LTI11AuthenticateHandler as LTIAuthenticateHandler, LTI11ConfigHandler as LTIConfigHandler
from modules.LTI11AuthenticateHandler import LTI11AuthenticateHandler as LTIAuthenticateHandler
from modules.LTI11LaunchValidator import LTI11LaunchValidator as LTILaunchValidator
#from ltiauthenticator.lti11.validator import LTI11LaunchValidator
from ltiauthenticator.utils import convert_request_to_dict, get_client_protocol
import os


class LTI11Authenticator(Authenticator):
    """
    JupyterHub Authenticator for use with LTI based services (EdX, Canvas, etc)
    """

    auto_login = True
    login_service = 'LTI'

    consumers = {
        os.environ["LTI_CLIENT_KEY"]: os.environ["LTI_SHARED_SECRET"]
    }

    def get_handlers(self, app):
        return [
            ('/lti/launch', LTIAuthenticateHandler)
        ]

    @gen.coroutine
    def authenticate(self, handler, data=None):
        # FIXME: Run a process that cleans up old nonces every other minute
        validator = LTILaunchValidator(self.consumers)

        args = {}
        for k, values in handler.request.body_arguments.items():
            args[k] = values[0].decode() if len(values) == 1 else [
                v.decode() for v in values]
            print(f"body_args: {k} => {values}")

        # handle multiple layers of proxied protocol (comma separated) and take the outermost
        if 'x-forwarded-proto' in handler.request.headers:
            # x-forwarded-proto might contain comma delimited values
            # left-most value is the one sent by original client
            hops = [h.strip()
                    for h in handler.request.headers['x-forwarded-proto'].split(',')]
            protocol = hops[0]
        else:
            protocol = handler.request.protocol

        #launch_url = protocol + "://" + handler.request.host + handler.request.uri
        launch_url = "https://" + handler.request.host + handler.request.uri

        if validator.validate_launch_request(
                launch_url,
                handler.request.headers,
                args
        ):
            # Before we return lti_user_id, check to see if a canvas_custom_user_id was sent.
            # If so, this indicates two things:
            # 1. The request was sent from Canvas, not edX
            # 2. The request was sent from a Canvas course not running in anonymous mode
            # If this is the case we want to use the canvas ID to allow grade returns through the Canvas API
            # If Canvas is running in anonymous mode, we'll still want the 'user_id' (which is the `lti_user_id``)

            canvas_id = handler.get_body_argument(
                'custom_canvas_user_id', default=None)

            if canvas_id is not None:
                user_id = handler.get_body_argument('custom_canvas_user_id')
            else:
                user_id = handler.get_body_argument('user_id')

            # Vor- und Nachname in der Form 'nachname_vorname':
            # user_name = handler.get_body_argument('lis_person_name_family') + "_" + handler.get_body_argument('lis_person_name_given')
            # Erster Teil der Mailadresse (alles vor dem '@'):
            #user_name = handler.get_body_argument('lis_person_contact_email_primary')
            #user_name = user_name.split("@")[0]  # '@...' entfernen
            user_name = handler.get_body_argument("ext_user_username")

            # Enable the formgrader and the course_list for instructors
            # Fix this if you want to have more extensions than nbgrader
            active = 'false'
            if handler.get_body_argument('roles') == 'Instructor':
                active = 'true'
            home_dir = '/home/jupyter-' + user_name
            jupyter_conf_dir = os.path.join(home_dir, '.jupyter')
            if os.path.exists(jupyter_conf_dir):
                path = os.path.join(jupyter_conf_dir, 'nbconfig', 'tree.json')
                os.makedirs(os.path.dirname(path), exist_ok=True)
                extensions = (
                    '{\n'
                    '  "load_extensions": {\n'
                    '    "formgrader/main": ' + active + ',\n'
                    '    "assignment_list/main": true,\n'
                    '    "course_list/main": ' + active + '\n'
                    '  }\n'
                    '}'
                )
                with open(path, 'w') as file:
                    file.write(extensions)

            # Create a log-file with required parameters for nbgrader
            # Exception handling if there are no LTI-Parameters for grade passback
            try:
                # 1. Create the path for the log-files
                course = str(handler.get_body_argument(
                    'context_label')).split(' ')[0].lower()
                assignment = handler.get_body_argument('resource_link_title')
                path = '/opt/tljh/exchange/' + course + '/inbound/log/' + \
                    assignment + '/jupyter-' + user_name + '.txt'
                os.makedirs(os.path.dirname(path), exist_ok=True)
                # 2. Store required_parameters for grade passback
                required_parameters = {
                    'lis_outcome_service_url': handler.get_body_argument('lis_outcome_service_url'),
                    'lis_result_sourcedid': handler.get_body_argument('lis_result_sourcedid')
                }
                # 3. Open the file and write the parameters
                with open(path, 'w') as file:
                    for key, value in required_parameters.items():
                        file.write(value + '\n')

            except:
                print("No LTI-Parameters for grade passback")

            os.environ['USER_ROLE'] = 'unknown'

            state = {
                'name': user_name,
                'auth_state': {k: v for k, v in args.items() if not k.startswith('oauth_')}
            }
            print(f"authenticate: {state}")
            return state

    def login_url(self, base_url):
        return url_path_join(base_url, '/lti/launch')