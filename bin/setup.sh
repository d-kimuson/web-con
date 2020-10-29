#!/bin/bash

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

git config core.hooksPath .githooks
if [ "$PIPENV_VENV_IN_PROJECT" = "1" ]; then
  bash -c "cd backend && pipenv run setup"
  bash -c "cd frontend && yarn install"
else
  echo "環境変数: PIPENV_VENV_IN_PROJECT=1を設定してください";
  exit 1;
fi

cd $PREVIOUS_DIRECTORY
