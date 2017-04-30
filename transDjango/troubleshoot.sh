#!/bin/bash
sleep 30
echo "fetching conflicts endpoint"
curl -X GET 'http://localhost:8000/transport/conflicts/'
# curl -X GET 'http://localhost:8000/transport/features/?source_name=Grind%20and%20Pave&startDate=2017-04-29&endDate=2020-01-01&format=json'
echo "got it"
