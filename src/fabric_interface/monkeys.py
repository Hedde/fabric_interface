__author__ = 'heddevanderheide'

import reversion

# App specific
from fabric_interface.formulae.models import Formula

reversion.register(Formula)
