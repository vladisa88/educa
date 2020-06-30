from .base import *


DEBUG = False

ADMINS = (
    ('Vladislav', '***'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

