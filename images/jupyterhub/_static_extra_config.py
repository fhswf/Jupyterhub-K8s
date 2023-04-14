import logging
import os
import sys

# ===========================================================================
#                            Extra Configuration
# ===========================================================================

print("loading extra conf: " + __file__)
#c.JupyterHub.template_paths = ['templates']

# Enable auth state to pass the authentication dictionary
# auth_state to the spawner
c.Authenticator.enable_auth_state = True

# auth
import MultiAuthenticator
from ltiauthenticator import LTIAuthenticator
from oauthenticator.generic import GenericOAuthenticator

# specific for multiauth:
# select login options
c.MultiAuthenticator.authenticators = [
    (LTIAuthenticator, "", False, {
        'LTI_CLIENT_KEY': "secretclientidforauth",
        'LTI_SHARED_SECRET': "somesharedsecret",
        'LTI13_PRIVATE_KEY': "/home/user/.ssh/private.pem",
    }),
    (GenericOAuthenticator, "keycloak", True, {
        'client_secret': 'supersecretclientkeyforencryption',
        'authorize_url': 'https://www.ki.fh-swf.de/keycloak/realms/kicluster/protocol/openid-connect/auth',
        'token_url': 'https://www.ki.fh-swf.de/keycloak/realms/kicluster/protocol/openid-connect/token',
        'userdata_url': 'https://www.ki.fh-swf.de/keycloak/realms/kicluster/protocol/openid-connect/userinfo',
        'login_service': 'keycloak',
        'username_key': 'preferred_username',
        'scope': ['openid'],
        'userdata_params': {'state': 'state'},           
    })
]
c.JupyterHub.authenticator_class = MultiAuthenticator
