import logging
from modules.MultiAuthenticator import MultiAuthenticator
import os
import sys

# ===========================================================================
#                            General Configuration
# ===========================================================================

c.JupyterHub.admin_access = True
c.JupyterHub.template_paths = ['templates']
c.Application.log_level = "DEBUG"
c.JupyterHub.log_level = logging.DEBUG

c.Authenticator.admin_users = {"admin"}
c.Authenticator.logout_redirect_url = os.environ['KEYCLOAK_LOGOUT_URL']

# Enable auth state to pass the authentication dictionary
# auth_state to the spawner
c.Authenticator.enable_auth_state = True

# Set the MultiAuthenticator as the authenticator
c.JupyterHub.authenticator_class = MultiAuthenticator


# ===========================================================================
#                            Docker Spawner Configuration
# ===========================================================================


c.Spawner.http_timeout = 120
c.Spawner.start_timeout = 300

# TODODO THIS IN KUBESPANER
#if "EXTRA_MOUNT_POINTS" in os.environ:
#    print("got extra mount points from env, reminder: do not use ',' or ':' in path. They are used to parse the string!")
#    extra_mount_points = [a.split(":") for a in os.environ.get('EXTRA_MOUNT_POINTS').split(",")]
#    for k, v in extra_mount_points:
#        c.DockerSpawner.volumes.update({k: v})


# c.Spawner.env_keep = ['LD_LIBRARY_PATH'] # set in DOCKERFILE of spawned container