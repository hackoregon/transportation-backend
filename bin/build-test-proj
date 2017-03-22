#! /bin/bash
usage() { echo "Usage: $0 [-l] for a local test or [-t] for a travis test " 1>&2; exit 1; }

while getopts ":lt" opt; do
    case "$opt" in
        l)
          docker-compose -f local-docker-compose.yml build
          docker-compose -f local-docker-compose.yml run \
          --entrypoint /code/bin/test-entrypoint.sh $DOCKER_IMAGE
           ;;
        t)
          docker-compose -f travis-docker-compose.yml build
          docker-compose -f travis-docker-compose.yml run \
          --entrypoint /code/bin/test-entrypoint.sh $DOCKER_IMAGE
          ;;
        *)
          usage
          ;;
    esac
done
