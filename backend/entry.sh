#!/bin/bash

# DB起動確認待ち
python manage.py check &> /dev/null  # 永遠に始まらないときは、標準出力して確認したほうが良い
STATUS_CODE=$?

until [ $STATUS_CODE = "0" ]; do
    python manage.py check &> /dev/null
    STATUS_CODE=$?
    echo "データベース起動待ち($STATUS_CODE)"
    sleep 1
done

# DBスキーマ変更をマイグレーションする
python manage.py migrate

# 静的ファイルの準備 (マウントの都合上、entryから準備する)
python manage.py collectstatic --noinput

# サーバー起動
echo "Django Application is ready to run."

gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
