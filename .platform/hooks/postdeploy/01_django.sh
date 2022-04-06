#!/bin/bash

source /var/app/venv/*/bin/activate && {

# collecting static files
python3 manage.py collectstatic --noinput;
# log which migrations have already been applied
python3 manage.py showmigrations;
# migrate the rest
python3 manage.py migrate --noinput;
# another command to create a superuser (write your own)
}