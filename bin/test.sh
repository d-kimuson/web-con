#!/bin/bash

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

# backend tests
cd backend
pipenv run test

# frontend tests
cd ../frontend
echo "テスト未登録"

cd $PREVIOUS_DIRECTORY
