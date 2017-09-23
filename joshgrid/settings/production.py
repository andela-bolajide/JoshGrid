"""Production specific settings."""
from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']
