from APIimports.models import Feature
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FeatureSerializer
from rest_framework import authentication, permissions
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from django.core.cache import cache

# Create your views here.


class FeatureView(generics.ListCreateAPIView):

    model = Feature
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()


class ConflictView(generics.ListCreateAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self, minDist=14):
        
        collisionGraph = cache.get('dateGraph')
        timePointSet = set()
        for u,v,d in collisionGraph.edges(data=True):
            if d['weight'] <= minDist:
                # print (u, v, d)
                if d['weight'] < minDist:
                    timePointSet = {u, v} | timePointSet
        
        pointSet = set()
        for idx, f in enumerate(timePointSet):
            print('idx', idx)
            closeFeat = Feature.objects.filter(geom__distance_lte=(f.geom, D(m=50)))
            pointSet = set(closeFeat) | pointSet


        return pointSet

    