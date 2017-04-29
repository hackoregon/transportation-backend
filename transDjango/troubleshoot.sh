#!/bin/bash
sleep 5
echo "fetching conflicts endpoint"
# curl -X GET --header 'Accept: application/json' --header 'X-CSRFToken: S4EntS1yRZ0Puo6mLA4VZQ3fMWyZ7EdNwEnwlVLUtywaPy09Llz4lNOGpM21jUBH' 'http://localhost:8000/transport/conflicts/'
curl -X GET --header 'Accept: text/html' --header 'X-CSRFToken: YEMk4i6IFzwPtJ8mCmHFbP0DkKop7mBTCevtWlQ4h82aOT29C7cOxML4XASrjCZN' 'http://localhost:8000/transport/nearby/'

echo "got it"
