FROM mysql:8.0


COPY initdb.d /docker-entrypoint-initdb.d
COPY my.cnf /etc/mysql/conf.d/my.cnf

ENV MYSQL_ROOT_PASSWORD password
ENV MYSQL_USER user
ENV MYSQL_PASSWORD password
ENV TZ "Asia/Tokyo"
