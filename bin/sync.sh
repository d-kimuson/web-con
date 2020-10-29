#!/bin/bash

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

bash -c "cd backend && pipenv run sync"
bash -c "cd frontend && yarn install"

cd $PREVIOUS_DIRECTORY
