from __future__ import unicode_literals
import os

if not os.environ.get('CI') and not os.environ.get('HEROKU'):
    from .development import *

if os.environ.get('HEROKU') is not None:
    from .production import *