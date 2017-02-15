from django.core.management.base import BaseCommand, CommandError
from psycopg2.extras import DateRange
from APIimports.models import Point, ApiElement
from django.contrib.gis.geos import GEOSGeometry
#from datetime import datetime
from dateutil import parser
import sys


class Command(BaseCommand):
    help = 'Import CIP points'

    # def add_arguments(self, parser):
    #     parser.add_argument('filePath', metavar='geojson file')

    def handle(self, *args, **options):
        sourceName = 'Capital Improv. Project - Points'
        apiModel = ApiElement.objects.filter(name=sourceName)[0]
        sourceJson = apiModel.payload
        #print(sourceJson)

        for feature in sourceJson['features']:
            # print(feature)
            start = feature['properties']['Est_Construction_Start_Date']
            end = feature['properties']['Est_Construction_Comp_Date']
            print(start, end)
            if end != None and start != None:
                start = parser.parse(start).date()
                end = parser.parse(end).date()
                if end >= start:
                    dateRange = DateRange(lower=start, upper=end)
                else:
                    dateRange = DateRange(lower=None, upper=None)
            else:
                    dateRange = DateRange(lower=None, upper=None)

            geom = GEOSGeometry(str(feature['geometry']))
            newPoint = Point(
                geom=geom,
                dateRange=dateRange,
                sourceRef=apiModel,
                data=feature['properties']
            )
            print(geom)
            print(dateRange)
            print(feature['properties'])
            newPoint.save()
            #sys.exit()
