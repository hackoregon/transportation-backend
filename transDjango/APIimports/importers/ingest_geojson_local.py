from APIimports.importers.ingest_geojson import jsonToPLP
from APIimports import constants
from APIimports.models import API_element
import os
import json

def load_local_json(importList):

    for apiName in importList:

        script_dir = os.path.dirname(__file__) 
        rel_path = constants.GEOJSON_META[apiName]['uri']
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, mode='r') as infile:
            data = json.load(infile)

        for name, metadata in constants.GEOJSON_META.items():

            if name == apiName:

                # Prevent duplicates for now.  Later we'll need to be
                # more sophisticated about how we handle repeated downloads
                if name in list(API_element.objects.values_list('api_name', flat=True)):
                    print("Skipped {} because it's already in the database.".format(name))
                    continue
    
                apiElement = API_element(
                    payload=data,
                    url=metadata['uri'],
                    api_name=name,
                    source_name=metadata['sourceName']
                )
                apiElement.save()

                passed_importList = [apiName]

                jsonToPLP(passed_importList, meta='GEOJSON_META')

