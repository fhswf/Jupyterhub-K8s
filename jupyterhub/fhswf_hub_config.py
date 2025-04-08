
import logging
import traitlets.log

# load the config object (satisfies linters)
c = get_config()  # noqa
logger = traitlets.log.get_logger()

# ===========================================================================
#           Extra Configuration deployment specific  
# ===========================================================================

def debug_auth(authenticator, handler, authentication):
    print(authenticator.__dict__)    
    print(handler.__dict__)      
    logger.info(f'Received auth state: {authentication.get("auth_state")}')
    return authentication

c.post_auth_hook_callbacks.append(debug_auth)