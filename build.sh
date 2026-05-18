#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Auto-create superuser from environment variables
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi