#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)

heroku container:push web
heroku container:release web
heroku logs -t

cd $PREVIOUS_DIRECTORY
