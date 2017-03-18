from APIimports.models import Point, Line, Polygon
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PointSerializer, LineSerializer, PolygonSerializer
from rest_framework import authentication, permissions

# Create your views here.


class PointView(generics.ListCreateAPIView):

    model = Point
    serializer_class = PointSerializer
    queryset = Point.objects.prefetch_related('sourceRef')


class LineView(generics.ListCreateAPIView):

    model = Line
    serializer_class = LineSerializer
    queryset = Line.objects.prefetch_related('sourceRef')


class PolygonView(generics.ListCreateAPIView):
    model = Polygon
    serializer_class = PolygonSerializer
    queryset = Polygon.objects.all()
