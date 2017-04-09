"""
Ingest HackOR geocoded data in .csv format to transdev database 
Needs to parse .csv files to geojson before anything can happen.
"""
from APIimports.importers.ingest_geojson import jsonToPLP
from APIimports import constants_local
from APIimports.models import API_element
import csv
import json
import datetime
import os

def csvToGeoJson(importList):
    #TODO: abstract this loading process
    
    for apiName in importList:
        print('loading {0}'.format(apiName))
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = constants_local.LOCAL_API_META[apiName]['uri']
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, mode='r') as infile:
            reader = csv.DictReader(infile)
            data = list(reader)

        geojson = {
                'type': 'FeatureCollection',
                'features' : []
            }

        for feature in data:
            
            build_features = {
                'type' : 'Feature',
                'properties' : {},
                'geometry' : {}
                }
                
            # Combines 'from_geojson' and 'to_geojson' into single MultiPoint geometry
            feat_geom = {
                'type' : 'MultiPoint', 
                'coordinates': [],
            }
                    
            # Extract relevant geojson
            coord_column = ['geojson_from', 'geojson_to']
            for coord in coord_column:
                try:
                    loaded_geojson = json.loads(feature[coord])
                    feat_geom['coordinates'].append(loaded_geojson['coordinates'])
                except:
                    continue
            build_features['geometry'] = feat_geom
            
            # Format other CSV columns into valid geojson property attributes
            metadata_columns = ['source_file_name', 'street', 'addy_from', 'addy_to' ,'start', 'finish']
            for column in metadata_columns:
                build_features['properties'][column] = feature[column]
            
            geojson['features'].append(build_features)

        #with open('test.json', 'w') as f:
        #    json.dump(geojson, f)
        geojsonLoader(importList, apiName, geojson)

def geojsonLoader(passed_importList, passed_apiName, converted_geojson):
    #loads converted csv to geojson data into our postgres database.
 
    print('loading {0} geojson'.format(passed_apiName))
    for name, metadata in constants_local.LOCAL_API_META.items():

        if name == passed_apiName:

            # Prevent duplicates for now.  Later we'll need to be
            # more sophisticated about how we handle repeated downloads
            if name in list(API_element.objects.values_list('api_name', flat=True)):
                print("Skipped {} because it's already in the database.".format(name))
                continue

            apiElement = API_element(
                payload=converted_geojson,
                url=metadata['uri'],
                api_name=name,
                source_name=metadata['sourceName']
            )
            apiElement.save()

            passed_importList = [passed_apiName]
            print(passed_importList)

            jsonToPLP(passed_importList, local=True)




#with open('test.json', 'w') as f:
#    json.dump(geojson, f)


