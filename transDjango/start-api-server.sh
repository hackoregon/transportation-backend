#!/bin/bash
cp /code/transDjango/settings_local_example.py /code/transDjango/settings_local.py
./manage.py migrate
./manage.py import_jsons
./manage.py jsonToCIPPoints
./manage.py jsonToCIPLines
./manage.py jsonToCIPPolygons
#./manage.py runserver
./manage.py runserver 0.0.0.0:8000
#gunicorn transDjango.wsgi:application -b :8000
