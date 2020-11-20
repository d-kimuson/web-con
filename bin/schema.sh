#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

bash -c "cd backend && pipenv run schema"
bash -c "cd frontend && yarn run openapi:gen"

# @ts-nocheck を挿入することで型エラーを無視します
function insertTsNocheck() {
  echo '// @ts-nocheck' | cat - $1 > temp && \mv temp $1
}

cd frontend/static/openapi
insertTsNocheck api.ts
insertTsNocheck base.ts

cd $PREVIOUS_DIRECTORY
