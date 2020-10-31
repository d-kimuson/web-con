#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin/

function setup_backend() {
  # database
  bash $BINARY_PATH/start_db.sh
  # django application
  pipenv run setup
}

function setup_frontend() {
  yarn install
}

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

git config core.hooksPath .githooks
if [ "$PIPENV_VENV_IN_PROJECT" = "1" ]; then
  cd backend && setup_backend
  cd ../frontend && setup_frontend
else
  echo "環境変数: PIPENV_VENV_IN_PROJECT=1を設定してください";
  exit 1;
fi

cd $PREVIOUS_DIRECTORY
