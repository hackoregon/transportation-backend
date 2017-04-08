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
"""
geojson = {
        'type': 'FeatureCollection',
        'features': [
        ]
    }
                        'type': 'Feature',
                    'properties' : {},
"""

counter = 0
for feature in data:
    # TODO: merge from_geojson and to_geojson
    feat_geom = {
        'type' : 'MultiPoint', 
        'coordinates': []
    }
            
    # Extract relevant geojson
    coord_column = ['geojson_from', 'geojson_to']
    for coord in coord_column:
        try:
            loaded_geojson = json.loads(feature[coord])
            feat_geom['coordinates'].append(loaded_geojson['coordinates'])
        except:
            continue

    feature['geometry'] = feat_geom

print(json.dumps(data[0]['geometry']))

















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