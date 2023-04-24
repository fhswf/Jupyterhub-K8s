import traitlets
import logging
from jupyterhub.auth import Authenticator
#from jupyterhub.handlers.login import LoginHandler, LogoutHandler
from jupyterhub.utils import url_path_join
#class MultiLoginHandler(LoginHandler):

#class MultiLogoutHandler(LogoutHandler):
    
class MultiAuthenticator(Authenticator):
    authenticators = traitlets.List(help="The subauthenticators to use", config=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        self._authenticators = []
        for authenticator_class, url_scope, display, configs in self.authenticators:
            c = self.trait_values()
            print(c)
            c.update(configs)
            self._authenticators.append({"instance": authenticator_class(**c), "url_scope": url_scope, "display": display})
    
    def get_handlers(self, app):
        """
        Gather all url routes from defined handlers in the authenticators.
        Note that some authenticators have multiple, such as the LTI.
        """
        routes = []
        for _authenticator in self._authenticators:
            for path, handler in _authenticator["instance"].get_handlers(app):

                class SubHandler(handler):
                    authenticator = _authenticator["instance"]

                routes.append((f'{_authenticator["url_scope"]}{path}', SubHandler))
        return routes
    
    def get_custom_html(self, base_url):
        """Render HTML login button"""
        html = []
        for authenticator in self._authenticators:
            print("authenticator")
            if hasattr(authenticator, "__dict__"):
                print(authenticator.__dict__) 
            if authenticator["display"] == True and "login_service" in authenticator["instance"].__dict__:
                login_service = authenticator["instance"].login_service
                url = url_path_join(base_url, authenticator["url_scope"], "oauth_login")
                html.append(
                    f"""
                    <div class="service-login">
                    <a role="button" class='btn btn-jupyter btn-lg' href='{url}'>
                        Sign in with {login_service}
                    </a>
                    </div>
                    """
            )
        return "\n".join(html)

    
    async def authenticate(self, handler, data):
        """Using the url of the request to decide which authenticator
        is responsible for this task.
        """
        return self._get_responsible_authenticator(handler).authenticate(handler, data)

    def get_callback_url(self, handler):
        return self._get_responsible_authenticator(handler).get_callback_url()

    # not sure if this is elegant
    def _get_responsible_authenticator(self, handler):
        responsible_authenticator = None
        for authenticator in self._authenticators:
            if handler.request.path.find(authenticator['url_scope']) != -1:
                self.log.info("redirect to ", authenticator["instance"].__name__) 
                responsible_authenticator = authenticator
                break
        return responsible_authenticator['instance']
