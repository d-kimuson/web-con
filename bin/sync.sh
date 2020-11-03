#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin

PREVIOUS_DIRECTORY=$(pwd)

cd $(git rev-parse --show-toplevel)/backend
bash $BINARY_PATH/start_db.sh
pipenv run sync

cd ../frontend
yarn install

cd $PREVIOUS_DIRECTORY
