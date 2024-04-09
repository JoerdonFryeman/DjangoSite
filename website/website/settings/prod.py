from .base import *
from os import environ, path

SECRET_KEY = str(environ.get('SECRET_KEY'))
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = str(environ.get('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(environ.get('EMAIL_HOST_PASSWORD'))
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': path.join(BASE_DIR, 'site_cache'),
    }
}
