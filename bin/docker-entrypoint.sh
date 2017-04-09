#!/bin/bash
export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn transDjango.wsgi:application -b :8000
