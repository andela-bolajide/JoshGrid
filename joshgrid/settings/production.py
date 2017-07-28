# Production specific settings
from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': dotenv.get('DATABASE_NAME'),
        'USER': dotenv.get('DATABASE_USER'),
        'PASSWORD': dotenv.get('DATABASE_PASSWORD'),
        'HOST': dotenv.get('DATABASE_HOST'),
        'PORT': dotenv.get('DATABASE_PORT'),
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
