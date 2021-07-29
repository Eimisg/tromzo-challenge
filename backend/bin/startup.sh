#!/bin/bash
echo $DJANGO_SETTINGS_MODULE

python3 manage.py collectstatic --noinput
python3 manage.py migrate -v 2 || exit 1
python3 manage.py runserver 0.0.0.0:8000
