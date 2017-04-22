"""
WSGI config for transDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import sys
import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transDjango.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)




# if bool(os.environ["DEBUG"]) == False:
#     from gevent import monkey;
#     from psycogreen.gevent import patch_psycopg
#
#     monkey.patch_all()
#     patch_psycopg()
