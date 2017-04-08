"""
Ingest HackOR geocoded data in .csv format to transdev database 
"""
#from APIimports import models
#from django.contrib.gis.geos import GEOSGeometry
#import logging
#from APIimports import constants
#import sys
import csv
import json


#def csvToPLP(importList):


with open('../management/commands/datafiles/tidy_geocoder_output.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    data = list(reader)
    #data = json.dumps([row for row in reader])

#print(data)

counter = 0
for feature in data:
    # TODO: merge from_geojson and to_geojson

    fc = {
        'type': 'FeatureCollection',
        'features': [
            {
            'type' : 'MultiPoint', 
            'coordinates': []
            }
        ]
    }
    
    # Extract relevant geojson
    geojson_list = ['geojson_from', 'geojson_to']
    for item in geojson_list:
        try:
            test = json.loads(feature['geojson_from'])
            print(test)
        except:
            continue
    #print(feature['geojson_from'])

    #fc['features'][0]['coordinates'].append(feature['geojson_from']['coordinates'])
    #fc['features'][0]['coordinates'].append(feature['geojson_to']['coordinates'])
    #counter += 1
    feature['geometry'] = fc

#print(data[0]['geometry'])

















"""
fc = {
        'type': 'FeatureCollection',
        'features': []
    }
    obj = json.loads(line)
    fc['features'].extend(obj['features'])
return fc
"""

#with open('output.json', mode='w') as outfile:
#    writer = csv.writer(outfile)
#    json.dump(data, outfile)

#'Geocoded Data - Misc Types': {
#    'uri': 'https://raw.githubusercontent.com/hackoregon/postgis-geocoder-test/master/Data/tidy_geocoder_output.csv',
#    'sourceName': 'City of Portland Geocoded Data',
#    'startDateField': None,
#    'endDateField': None,
#    'status': None,