from APIimports.models import Point
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PointSerializer
from rest_framework import authentication, permissions


# Create your views here.




# class PointViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Point.objects.all()
#     serializer_class = PointSerializer

# class PointView(APIView):

#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (permissions.AllowAny,)

#     def get(self, request, format=None):
#         points = Point.objects.all()
#         return Response(points)

class PointView(generics.ListCreateAPIView):
    model = Point
    serializer_class = PointSerializer
    queryset = Point.objects.all()
