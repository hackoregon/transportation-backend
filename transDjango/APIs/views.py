from APIimports.models import Feature, AddressGeocode
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FeatureSerializer
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.gis.geos import GEOSGeometry
from dateutil import parser
from psycopg2.extras import DateRange
from django.contrib.gis.measure import D
import datetime
from .viewUtils import getMinDist
import sys

# Create your views here.


class FeatureView(generics.ListAPIView):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('source_name',)

class FeatureDetailView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class ConflictView(generics.ListAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        minDist = getMinDist(self.request, 'distance', 100)
        minDays = getMinDist(self.request, 'days', 14)
        
        collisionGraph = cache.get('featureGraph')
        featureSet = set()
        for u, v, d in collisionGraph.edges(data=True):

            if d['daysApart'] <= minDays and d['distance'] <= minDist:
                featureSet = {u, v} | featureSet

        return featureSet


class NearbyProjects(generics.ListAPIView):
    serializer_class = FeatureSerializer
    
    def get_queryset(self):
        minDist = getMinDist(self.request, 'distance', 100)
        minDays = getMinDist(self.request, 'days', 14)
        queryDate = parser.parse(self.request.query_params['date']).date()
        startDate = queryDate - datetime.timedelta(days=minDays)
        endDate = queryDate + datetime.timedelta(days=minDays)
        queryDateRange = DateRange(startDate, endDate)        
        geoaddy = AddressGeocode.objects.using('geocoder').raw("SELECT g.rating, ST_X(g.geomout) AS lon, ST_Y(g.geomout) AS lat, pprint_addy(addy) AS address FROM geocode(%s) as g LIMIT 1", [self.request.query_params['address']])[0]
        queryPoint = GEOSGeometry('POINT({} {})'.format(geoaddy.lon, geoaddy.lat))
        return Feature.objects.filter(canonical_daterange__overlap=queryDateRange).filter(geom__distance_lte=(queryPoint, D(m=minDist)))

