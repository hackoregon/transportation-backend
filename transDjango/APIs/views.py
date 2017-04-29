from APIimports.models import Feature, AddressGeocode
from rest_framework import generics
from .serializers import FeatureSerializer
from django.core.cache import cache
from django.contrib.gis.geos import GEOSGeometry
from dateutil import parser
from psycopg2.extras import DateRange
from django.contrib.gis.measure import D
import datetime
import sys
from django.db import DataError

# Create your views here.


class FeatureView(generics.ListAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self,):
        params = self.request.query_params

        showNulls = params.get('showNulls', None)

        sourceName = params.get('source_name', None)

        filteredFeatures = Feature.objects.all()
        if sourceName:
            filteredFeatures = filteredFeatures.filter(source_name=sourceName)

        defaultRange = 180
        defaultStart = datetime.date.today() - datetime.timedelta(days=2)
        defaultEnd = defaultStart + datetime.timedelta(days=defaultRange)
        startDate = params.get('startDate', None)
        endDate = params.get('endDate', None)    

        if startDate or endDate:
            if startDate and endDate:
                try:
                    queryDateRange = DateRange(lower=startDate, upper=endDate)
                except DataError:
                    queryDateRange = DateRange(lower=defaultStart, upper=defaultEnd)
            elif startDate:
                calcEnd = parser.parse(startDate) + datetime.timedelta(days=3)
                queryDateRange = DateRange(lower=startDate, upper=calcEnd)
            else:
                queryDateRange = DateRange(lower=defaultStart, upper=defaultEnd)

            filteredFeatures = filteredFeatures.filter(canonical_daterange__overlap=queryDateRange)

        elif not showNulls:
            filteredFeatures = filteredFeatures.exclude(canonical_daterange=None).exclude(canonical_daterange__isempty=True)
            
        print('featurecount', filteredFeatures.count())
        return filteredFeatures


class FeatureDetailView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class ConflictView(generics.ListAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        params = self.request.query_params
        
        excludeStatuses = ['COMPLETED', 'COMPLETED', 'COMPLETE', 'DENIED', 'CANCELED']
        
        minDist = int(params.get('distance', 100))
        
        minDays = int(params.get('days', 14))
        
        defaultStart = datetime.date.today() - datetime.timedelta(days=2)
        defaultEnd = defaultStart + datetime.timedelta(days=180)
        startDate = params.get('startDate', defaultStart.isoformat())
        endDate = params.get('endDate', defaultEnd.isoformat())
        queryDateRange = DateRange(lower=startDate, upper=endDate)
        excludeDateRange = DateRange(lower='1800-01-01', upper='2014-12-31')
        
        collisionGraph = cache.get('featureGraph')
        featureIDs = set()
        for u, v, d in collisionGraph.edges(data=True):
            if d['daysApart'] <= minDays and d['distance'] <= minDist:
                # if u in [63400, 66403] and v in [63400, 66403]:
                #     print('uvd', u, v, d)
                featureIDs = {u, v} | featureIDs
        
        filteredFeatures = Feature.objects\
            .filter(pk__in=featureIDs)\
            .filter(canonical_daterange__overlap=queryDateRange)\
            .exclude(canonical_daterange__overlap=excludeDateRange)\
            .exclude(canonical_status__in=excludeStatuses)

        print('featurecount', filteredFeatures.count())

        return filteredFeatures

class NearbyProjects(generics.ListAPIView):
    serializer_class = FeatureSerializer
    
    def get_queryset(self):
        params = self.request.query_params
        excludeStatuses = ['COMPLETED', 'COMPLETED', 'COMPLETE', 'DENIED', 'CANCELED']
        minDist = params.get('distance', 100)
        defaultStart = datetime.date.today() - datetime.timedelta(days=2)
        defaultEnd = defaultStart + datetime.timedelta(days=365)
        startDate = params.get('startDate', defaultStart.isoformat())
        endDate = params.get('endDate', defaultEnd.isoformat())
        queryDateRange = DateRange(lower=startDate, upper=endDate)
        excludeDateRange = DateRange(lower='1800-01-01', upper='2014-12-31')
        geoaddy = AddressGeocode.objects.using('geocoder').raw("SELECT g.rating, ST_X(g.geomout) AS lon, ST_Y(g.geomout) AS lat, pprint_addy(addy) AS address FROM geocode(%s) as g LIMIT 1", [self.request.query_params['address']])[0]
        queryPoint = GEOSGeometry('POINT({} {})'.format(geoaddy.lon, geoaddy.lat))
        filteredFeatures = Feature.objects\
            .filter(canonical_daterange__overlap=queryDateRange)\
            .filter(geom__distance_lte=(queryPoint, D(m=minDist)))\
            .exclude(canonical_daterange__overlap=excludeDateRange)\
            .exclude(canonical_status__in=excludeStatuses)

        print('featurecount', filteredFeatures.count())

        return filteredFeatures

