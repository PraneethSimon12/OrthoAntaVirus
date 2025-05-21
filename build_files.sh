#!/usr/bin/env bash
set -e

echo "BUILD START"

# install Python dependencies
python3.12 -m pip install -r requirements.txt

# collect all the Django static files into STATIC_ROOT
python3.12 manage.py collectstatic --noinput --clear

echo "BUILD END"
