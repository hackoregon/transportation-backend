from APIimports.models import Neighborhood
from django.contrib.gis.geos import GEOSGeometry
import os
import json

def load_neighborhoods():

    if Neighborhood.objects.count() > 0:
        print("The neighborhood data has aleady been loaded, skipping neighborhood loading.")

    else:
        script_dir = os.path.dirname(__file__) 
        rel_path = '../management/commands/datafiles/neighborhoods.geojson'
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, mode='r') as infile:
            data = json.load(infile)

        for d in data['features']:
            print(d['properties']['NAME'])
            print(d['properties']['MAPLABEL'])
            print(d['geometry'])
            geom = GEOSGeometry(str(d['geometry']))
            neighborhood = Neighborhood(
                geom=geom,
                name=d['properties']['NAME'],
                label=d['properties']['MAPLABEL'],
            )
            neighborhood.save()
