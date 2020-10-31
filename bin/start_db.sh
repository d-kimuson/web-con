#!/bin/bash

BINARY_PATH=$(git rev-parse --show-toplevel)/bin/

cd $(git rev-parse --show-toplevel)/backend/db && make start && STATUS_CODE=$?
if [ "$STATUS_CODE" != "0" ]; then make restart; fi
$BINARY_PATH/wait_db.sh
