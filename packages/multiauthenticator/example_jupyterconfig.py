import logging
import os
import sys
from ltiauthenticator import LTIAuthenticator
import MultiAuthenticator
from oauthenticator.generic import GenericOAuthenticator
# ===========================================================================
#                            Extra Configuration
# ===========================================================================

print("loading extra conf: " + __file__)

# global config still works
c.Authenticator.enable_auth_state = True

# specific for multiauth:
# select login options
c.MultiAuthenticator.authenticators = [
    (LTIAuthenticator, "lti", False, {
        "consumers": {"<lti_client_key>": "<lti_shared_secret>"}
    }),
    (GenericOAuthenticator, "oauth", True, {
        "client_secret": "supersecretclientkeyforencryption",
        "authorize_url": "<host>/oidc/cluster/protocol/openid-connect/auth",
        "token_url": "<host>/oidc/cluster/protocol/openid-connect/token",
        "userdata_url": "<host>/oidc/cluster/protocol/openid-connect/userinfo",
        "login_service": "oauth",
        "username_key": "preferred_username",
        "scope": ["openid"],
        "userdata_params": {"state": "state"},           
    })
]

c.JupyterHub.authenticator_class = MultiAuthenticator