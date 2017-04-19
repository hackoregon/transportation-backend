'''
Configuration for the Hack Oregon Transportation project backend Django app in the INTEGRATION environment
'''

import os # enables access to environment variables

AWS = {
    'ENGINE': '',
    'NAME': '',
    'HOST': '',
    'PORT': '',
    'USER': '',
    'PASSWORD': '',
    }

GEOCODER = {
    'ENGINE': '',
    'NAME': '',
    'HOST': '',
    'PORT': '',
    'USER': '',
    'PASSWORD': '',
    }

DEFAULT = {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'transdev',
    'HOST': 'localhost',
    'PORT': '5432',
    'USER': 'transdev',
    'PASSWORD': 'password',
}


DJANGO_SECRET_KEY = 'yourSecretKeyHere'

# Note: the 192.168.99.100 address is necessary to enable testing with Docker Toolbox for Mac and Windows
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

DEBUG = True
