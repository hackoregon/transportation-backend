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


# class PointView(generics.ListCreateAPIView):

#     model = Point
#     serializer_class = PointSerializer
#     queryset = Point.objects.prefetch_related('sourceRef')


# class LineView(generics.ListCreateAPIView):

#     model = Line
#     serializer_class = LineSerializer
#     queryset = Line.objects.prefetch_related('sourceRef')


# class PolygonView(generics.ListCreateAPIView):
#     model = Polygon
#     serializer_class = PolygonSerializer
#     queryset = Polygon.objects.prefetch_related('sourceRef')


class ConflictView(generics.ListCreateAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self, minDist=14):
        
        collisionGraph = cache.get('dateGraph')
        pointset = set()
        for u,v,d in collisionGraph.edges(data=True):
            if d['weight'] <= minDist:
                # print (u, v, d)
                if d['weight'] < minDist:
                    pointset = {u, v} | pointset
                    
        return pointset

    