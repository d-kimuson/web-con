#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

git config core.hooksPath .githooks
if [ "$PIPENV_VENV_IN_PROJECT" = "1" ]; then
  cd backend && pipenv run setup
  bash $BINARY_PATH/sync.sh
else
  echo "環境変数: PIPENV_VENV_IN_PROJECT=1を設定してください";
  exit 1;
fi

cd $PREVIOUS_DIRECTORY
