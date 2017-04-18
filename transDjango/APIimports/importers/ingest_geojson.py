from psycopg2.extras import DateRange
from APIimports import models
from django.contrib.gis.geos import GEOSGeometry
from dateutil import parser
import logging
from APIimports import constants
import sys


logger = logging.getLogger(__name__)


def jsonToPLP(importList, meta='API_META'):

    # Distinguish between data downloaded from external API and local data files.
    for apiName in importList:
        if meta == 'API_META':
            metadata = constants.API_META[apiName]
        if meta == 'CSV_META':
            metadata = constants.CSV_META[apiName]
        if meta == 'GEOJSON_META':
            metadata = constants.GEOJSON_META[apiName]            

        apiModel = models.API_element.objects.filter(api_name=apiName)[0]
        sourceJson = apiModel.payload
        #print(sourceJson)

        counter = 0
        for feature in sourceJson['features']:
            counter += 1
            # print(feature)

            # Make the dateRange from the API specific start and end date fields
            # startFieldKey = metadata['startDateField']
            # endFieldKey = metadata['endDateField']
            start = feature['properties'][metadata['startDateField']]
            end = feature['properties'][metadata['endDateField']]
            #print(start, end)
            if end and start:
                start = parser.parse(start).date()
                end = parser.parse(end).date()
                if end >= start:
                    dateRange = DateRange(lower=start, upper=end)
                else:
                    dateRange = None
            else:
                    dateRange = None

            # Make the Geometry
            geom = GEOSGeometry(str(feature['geometry']))
            if geom.geom_type not in ['Point', 'MultiPoint', 'LineString', 'MultiLineString', 'Polygon', 'MultiPolygon']:
                print("Could not identify geometry type: {}.  Exiting.".format(geom.geom_type))
                sys.exit()

            try:
                status = feature['properties'][metadata['status']]
            except:
                status = ''

            try:
                hood = models.Neighborhood.objects.filter(geom__intersects=geom)[0]
            except IndexError:
                hood = None

            newPoint = models.Feature(
                geom=geom,
                orig_daterange=dateRange,
                canonical_daterange=dateRange,
                orig_status=status,
                canonical_status=status,
                source_ref=apiModel,
                source_name=apiModel.source_name,
                data=feature['properties'],
                neighborhood=hood,
            )
            # print ("Save")
            newPoint.save()
