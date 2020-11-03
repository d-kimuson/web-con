#!/bin/bash

PREVIOUS_DIRECTORY=$(pwd)
cd $(git rev-parse --show-toplevel)/backend/db

make connect_check &> /dev/null
STATUS_CODE=$?

until [ $STATUS_CODE = "0" ]; do
  make connect_check &> /dev/null
  STATUS_CODE=$?
  echo "データベース起動待ち($STATUS_CODE)"
  sleep 1
done

echo "データベースの起動を確認"
cd $PREVIOUS_DIRECTORY
