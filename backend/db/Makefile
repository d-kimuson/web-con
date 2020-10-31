SHELL=/bin/bash
CONT_NAME := web_con_mysql
IMAGE_NAME := web_con_mysql
DB_NAME := web_con_django
DB_USER := user
DB_PSWD := password

start:
	# 起動済みコンテナ or ビルド済みのイメージがあればそのまま使う
	# ない場合は、ビルドして起動する
	if [ "`docker images | grep -c $(IMAGE_NAME)`" = "0" ]; then make _build; fi
	if [ "`docker ps | grep -c $(CONT_NAME)`" = "0" ]; then make _start; fi

restart:
	# 起動済みのコンテナ&イメージを廃棄して、起動する
	make stop && make remove
	make start

stop:
	docker stop $(CONT_NAME)
	docker rm $(CONT_NAME)

remove:
	docker rmi $(IMAGE_NAME)

connect:
	mysql $(DB_NAME) -h127.0.0.1 -u$(DB_USER) -p$(DB_PSWD)

connect_check:
	# テストで起動確認に使う
	mysql $(DB_NAME) -h127.0.0.1 -u$(DB_USER) -p$(DB_PSWD) -e ""

_build:
	docker build . -t $(IMAGE_NAME)

_start:
	docker run -p 3306:3306 --name $(CONT_NAME) -d $(IMAGE_NAME)
