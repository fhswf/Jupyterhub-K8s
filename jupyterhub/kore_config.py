# load the config object (satisfies linters)
c = get_config()  # noqa

import logging
import os
import sys

from ltiauthenticator import LTIAuthenticator

# ===========================================================================
#              Extra Configuration kore server extension  
# ===========================================================================

print("loading kore extension conf: " + __file__)

