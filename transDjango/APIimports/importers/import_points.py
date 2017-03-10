from psycopg2.extras import DateRange
from APIimports import models
from django.contrib.gis.geos import GEOSGeometry
from dateutil import parser
import logging
from APIimports import constants
import sys


logger = logging.getLogger(__name__)


def jsonToPoints(importList):


    for apiName in importList:

        metadata = constants.API_META[apiName]

        apiModel = models.ApiElement.objects.filter(apiName=apiName)[0]
        sourceJson = apiModel.payload
        #print(sourceJson)

        for feature in sourceJson['features']:
            # print(feature)
            startFieldName = metadata['startDateField']
            endFieldName = metadata['endDateField']
            start = feature['properties'][startFieldName]
            end = feature['properties'][endFieldName]
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
            if geom.geom_type == 'Point':
                model = getattr(models, 'Point')
            elif geom.geom_type in ('LineString', 'MultiLineString'):
                model = getattr(models, 'Line')
            elif geom.geom_type in ('Polygon', 'MultiPolygon'):
                model = getattr(models, 'Polygon')
            else:
                print("Could not identify geometry type: {}.  Exiting.".format(geom.geom_type))
                sys.exit()
            
            newPoint = model(
                geom=geom,
                dateRange=dateRange,
                sourceRef=apiModel,
                data=feature['properties']
            )

            newPoint.save()
