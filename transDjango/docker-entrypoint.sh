#!/bin/bash
echo  "Running docker-entrypoint.sh... from transDjango/bin"
#export PATH=$PATH:~/.local/bin
# python manage.py migrate --noinput

./getconfig.sh
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# gunicorn transDjango.wsgi:application -b :8000
./troubleshoot.sh &

# Fire up a lightweight frontend to host the Django endpoints - gunicorn was the default choice
# gevent used to address ELB/gunicorn issue here https://github.com/benoitc/gunicorn/issues/1194
gunicorn transDjango.wsgi:application -b :8000 --worker-class 'gevent' --workers 1
