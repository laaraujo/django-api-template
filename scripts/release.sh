#!/bin/bash
python manage.py spectacular --color --file schema.yml
python manage.py collectstatic --noinput
python manage.py migrate
