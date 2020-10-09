#!/bin/bash


set -e
cd "$(dirname "${BASH_SOURCE[0]}")/.."


uwsgi --http :8000 --module project.wsgi
