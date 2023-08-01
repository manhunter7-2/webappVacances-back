#!/usr/bin/env bash
# exit on error

/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate