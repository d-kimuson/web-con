#!/bin/bash

git config core.hooksPath .githooks
bash -c "cd backend && pipenv run setup"
bash -c "cd frontend && yarn install"
