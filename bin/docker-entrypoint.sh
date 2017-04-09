#!/bin/bash
export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
pwd
ls -la
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn homelessAPI.wsgi:application -b :8000
