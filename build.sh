#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt


/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip


python manage.py collectstatic --no-input
python manage.py migrate