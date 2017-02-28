FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update
#RUN apt-get -y install sudo
RUN apt-get -y install gdal-bin
RUN apt-get -y install libgeoip1
#RUN apt-get -y install postgresql-9.5-postgis-2.2
ADD ./requirements.txt /provision/
WORKDIR /provision/
RUN pip install -r requirements.txt
WORKDIR /code/
