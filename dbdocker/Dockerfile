FROM postgres:9.5.5
USER root
RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install gdal-bin
RUN apt-get -y install libgeoip1
RUN apt-get -y install postgresql-9.5-postgis-2.2
WORKDIR /code/
