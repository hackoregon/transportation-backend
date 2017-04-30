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

# Monkey patching the application to help stabilize the Docker container deploy
# Deploying Docker containers to ECS often timed out and the new container would get killed by ALB
# That problem disappeared completely once this monkey patching was implemented
from psycogreen.gevent import patch_psycopg
from gevent import monkey; monkey.patch_all()
# from gevent import monkey; monkey.patch_all(thread=False)

patch_psycopg()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transDjango.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)




# if bool(os.environ["DEBUG"]) == False:
#     from gevent import monkey;
#     from psycogreen.gevent import patch_psycopg
#
#     monkey.patch_all()
#     patch_psycopg()
