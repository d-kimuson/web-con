#!/bin/bash

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

function check() {
  if [ $? -eq 0 ];then
    echo "問題なし ($1)"
  else
    echo "$1 で問題が発生しました" >&2
    exit 1
  fi
}

# backend checks
./backend/.venv/bin/mypy --config-file ./backend/mypy.ini ./backend; check "mypy"
cd backend
./.venv/bin/python manage.py check; check "Django"
./.venv/bin/autopep8 -i ./**/*.py
./.venv/bin/flake8 .; check "flake8"

# frontend checks
cd ../frontend
yarn lint && check "eslint & stylelint"

cd $PREVIOUS_DIRECTORY
