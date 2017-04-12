#!/bin/bash
export PATH=$PATH:~/.local/bin
# python manage.py migrate --noinput
# python manage.py collectstatic --noinput
# gunicorn transDjango.wsgi:application -b :8000
gunicorn budget_proj.wsgi:application -b :8000 --keep-alive 60 --worker-class 'gevent' # gevent used to address ELB/gunicorn issue here https://github.com/benoitc/gunicorn/issues/1194
