#!/bin/bash
# cp /code/transDjango/settings_local_example.py /code/transDjango/settings_local.py

sleep 100000
./manage.py migrate
./manage.py createcachetable
# ./manage.py import_jsons
#  ./manage.py ingest_jsons
#./manage.py runserver
./manage.py runserver 0.0.0.0:8000
# gunicorn transDjango.wsgi:application -b :8000
