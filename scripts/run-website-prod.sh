#!/bin/bash


set -e
cd "$(dirname "${BASH_SOURCE[0]}")/.."


uwsgi --http :80 --module project.wsgi
