from django.core.management.base import BaseCommand, CommandError
from psycopg2.extras import DateRange
from APIimports.models import Polygon, ApiElement
from django.contrib.gis.geos import GEOSGeometry
from dateutil import parser
import sys


class Command(BaseCommand):
    help = 'Import CIP Polygons'

    def handle(self, *args, **options):
        sourceName = 'Capital Improv. Project - Polygons'
        apiModel = ApiElement.objects.filter(name=sourceName)[0]
        sourceJson = apiModel.payload

        for feature in sourceJson['features']:
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
            newPolygon = Polygon(
                geom=geom,
                dateRange=dateRange,
                sourceRef=apiModel,
                data=feature['properties']
            )

            newPolygon.save()