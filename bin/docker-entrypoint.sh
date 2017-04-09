#!/bin/bash
export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
pwd
ls -la
python transDjango/manage.py migrate --noinput
python transDjango/manage.py collectstatic --noinput
gunicorn transDjango.wsgi:application -b :8000
