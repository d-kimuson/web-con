#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

# requirements.txt を生成
cd backend
rm -f requirements.txt && pipenv lock -r > requirements.txt

cd ..
heroku container:push web

if [ $? = "0" ]; then
  heroku container:release web
  heroku logs -t
fi

cd $PREVIOUS_DIRECTORY
