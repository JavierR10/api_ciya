
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
        'NAME': 'ciyadatabase',
        'USER': 'postgres',
        'PASSWORD': 'xpango2011',
        'HOST': 'ciyadbaws.cakcdqyqgv2b.us-east-1.rds.amazonaws.com', # IP DE DOCKER -- localhost
        'PORT': '5432', #PUERTO DE DOCKER -- 5433
        'OPTIONS': {
            'options': '-c search_path=public,laboratorios,investigacion,academico,seguridades,vinculacion'
        },
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
