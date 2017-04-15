FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get -y install gdal-bin
RUN apt-get -y install libgeoip1
# ADD ./requirements.txt /provision/
WORKDIR /code/
ADD . /code/
RUN pip install -r requirements.txt
ENTRYPOINT [ "/code/docker-entrypoint.sh" ]
