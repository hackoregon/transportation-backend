#! /bin/bash
usage() { echo "Usage: $0 [-l] for a local build or [-t] for a travis build " 1>&2; exit 1; }

while getopts ":lt" opt; do
    case "$opt" in
        l)
          docker-compose -f local-docker-compose.yml build
          ;;
        t)
          docker-compose -f travis-docker-compose.yml build
          ;;
        *)
          usage
          ;;
    esac
done
