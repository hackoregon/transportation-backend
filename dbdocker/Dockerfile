FROM postgres:9.5.5
USER root
RUN apt-get update
RUN apt-get -y install postgresql-9.5-postgis-2.2
COPY ./setupdb.sql /docker-entrypoint-initdb.d/10-setupdb.sql
