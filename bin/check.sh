#!/bin/bash

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

# backend checks
./backend/.venv/bin/mypy --config-file ./backend/mypy.ini ./backend  # mypy
cd backend
./.venv/bin/python manage.py check                                   # Django
./.venv/bin/flake8 .                                                 # flake8

# frontend checks
cd ../frontend
yarn lint

cd $PREVIOUS_DIRECTORY
