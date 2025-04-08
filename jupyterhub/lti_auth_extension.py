# load the config object (satisfies linters)
c = get_config()  # noqa

import logging
import os
import sys

from ltiauthenticator import LTIAuthenticator

# ===========================================================================
#              Extra Configuration for  LTI AUTH and nbgrader  
# ===========================================================================

print("loading lti auth extension conf: " + __file__)



#-------------------------------------------------------------------------------
# post_auth_hook
#-------------------------------------------------------------------------------

c.post_auth_hook_callbacks = []

# fhswf: Note that not all authenticators are LTI or Simililar, so this is already very specific
# i like the idea of having mutliple hooks though, so this is a a keep
async def post_auth_callback(authenticator, handler, authentication: dict) -> dict:
    """
    Optional hook to run necessary bootstrapping tasks.
    If any of these tasks returns `True` the JupyterHub will be restarted.

    Parameters
    ----------
    authenticator : LTI13Authenticator
        The JupyterHub LTI 1.3 Authenticator.
    handler : LTI13CallbackHandler
        Handles JupyterHub authentication requests responses according to the LTI 1.3 standard.
    authentication : dict
        The authentication dict for the user.

    Returns
    -------
    dict
        The (altered) authentication dict for the user.

    Notes
    -----
        The username on Debian has to start with a letter, which is why the letter u is prefixed.
    """
    
    logging.debug('Running post authentication hooks')
    # fhswf: not sure where something specific like this could be stored:
    restart_on_bool_response:bool = False
    
    needs_restart  = False
    authentication['name'] = 'u' + authentication['name']    # usernames have to start with a-z on Debian
    for callback in c.post_auth_hook_callbacks:
        if await callback(authenticator, handler, authentication):
            needs_restart = True

    logging.debug('Finished post authentication hooks. Needs restart: ' + str(needs_restart))

    if needs_restart and restart_on_bool_response:
        logging.info('restarting hub in 5 seconds...')
        # fhswf: This should nopt hardwire to systemd, but i am not sure how this could even work for other deployments like any non systemd podman.
        subprocess.run(['systemd-run', '--on-active=5', 'systemctl', 'restart', 'jupyterhub'])
    
    return authentication

c.Authenticator.post_auth_hook = post_auth_callback


def populate_auth_state(authenticator, handler, auth_model):

    if auth_model['auth_state'] is None:
        auth_model['auth_state'] = {}
    auth_model['auth_state']['lti-auth-data'] = {}

    return auth_model

c.post_auth_hook_callbacks.append(populate_auth_state)