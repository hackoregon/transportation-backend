FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get -y install gdal-bin
RUN apt-get -y install libgeoip1
WORKDIR /code/
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
ENTRYPOINT [ "/code/docker-entrypoint.sh" ]
