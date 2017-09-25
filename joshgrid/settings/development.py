"""Development specific settings."""
import os
import sys

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': dotenv.get('DATABASE_NAME'),
            'USER': dotenv.get('DATABASE_USER'),
            'PASSWORD': dotenv.get('DATABASE_PASSWORD'),
            'HOST': dotenv.get('DATABASE_HOST'),
            'PORT': dotenv.get('DATABASE_PORT'),
        }
    }
