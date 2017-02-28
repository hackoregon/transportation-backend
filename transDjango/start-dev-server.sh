#!/bin/bash


# Make sure data is only loaded on first start
if [ ! -d /data ]; then

  echo "Downloading data..."

  cp /code/transDjango/settings_local_example.py /code/transDjango/settings_local.py

  ./manage.py import_jsons
  ./manage.py jsonToCIPPoints
  ./manage.py jsonToCIPLines
  ./manage.py jsonToCIPPolygons

fi

./manage.py runserver
