#!/bin/bash


set -e
cd "$(dirname "${BASH_SOURCE[0]}")/.."

sudo /etc/init.d/nginx restart
uwsgi --socket mysite.sock --module project.wsgi --chmod-socket=666
