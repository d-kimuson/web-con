SHELL=/bin/bash
CONT_NAME := web_con_mysql
IMAGE_NAME := web_con:mysql_db
DB_NAME := web_con_django
DB_USER := user
DB_PSWD := password

start:
	if [ "`docker ps | grep -c $(CONT_NAME)`" != "0" ]; then make stop; fi
	docker build -t $(IMAGE_NAME) .
	docker run -p 3306:3306 --name $(CONT_NAME) -d $(IMAGE_NAME)

stop:
	docker stop $(CONT_NAME)
	docker rm $(CONT_NAME)

connect:
	mysql $(DB_NAME) -h127.0.0.1 -u$(DB_USER) -p$(DB_PSWD)
