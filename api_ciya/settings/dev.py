
import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ciya',
        'USER': 'postgres',
        'PASSWORD': 'ads450nb',
        'HOST': '0.0.0.0', # IP DE DOCKER -- localhost
        'PORT': '5422', #PUERTO DE DOCKER -- 5433
        'OPTIONS': {
            'options': '-c search_path=public,laboratorios,investigacion'
        },
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
