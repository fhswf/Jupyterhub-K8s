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
