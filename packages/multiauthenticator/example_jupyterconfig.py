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
    (LTIAuthenticator), None, {
        'client_id': 'xxxx',
        'client_secret': 'xxxx',
        'oauth_callback_url': 'http://example.com/hub/github/oauth_callback'
    }
    (GenericOAuthenticator), None, {
        'client_id': 'xxxx',
        'client_secret': 'xxxx',
        'oauth_callback_url': 'http://example.com/hub/github/oauth_callback'
    }
]

c.JupyterHub.authenticator_class = MultiAuthenticator