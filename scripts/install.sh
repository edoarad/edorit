#!/bin/bash


set -e
cd "$(dirname "${BASH_SOURCE[0]}")/.."


python -m virtualenv .env --prompt='[edorit] '
.env/bin/pip install -U pip
.env/bin/pip install -r requirements.txt

python3 manage.py makemigrations website
python3 manage.py migrate