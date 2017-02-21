from APIimports.models import Point, Line
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PointSerializer, LineSerializer
from rest_framework import authentication, permissions

# Create your views here.


class PointView(generics.ListCreateAPIView):
    model = Point
    serializer_class = PointSerializer
    queryset = Point.objects.all()


class LineView(generics.ListCreateAPIView):
    model = Line
    serializer_class = LineSerializer
    queryset = Line.objects.all()
