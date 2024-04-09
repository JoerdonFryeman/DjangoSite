from .base import *
from os import environ

SECRET_KEY = str(environ.get('SECRET_KEY'))
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
