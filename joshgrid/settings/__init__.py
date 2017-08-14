"""Define settings using values of environment variables."""

import os

if os.environ.get('CI'):
    from .test import *

if not os.environ.get('CI') and not os.environ.get('HEROKU'):
    from .development import *

if os.environ.get('HEROKU'):
    from .production import *
