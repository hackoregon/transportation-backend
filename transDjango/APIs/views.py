from APIimports.models import Feature
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FeatureSerializer
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class FeatureView(generics.ListCreateAPIView):

    model = Feature
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('source_name',)


class ConflictView(generics.ListCreateAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        # print('get method', self.request.query_params.get('days', 14))
        defaultDist = 100
        defaultDays = 14
        try:
            minDays = int(self.request.query_params.get('days', defaultDays))
        except ValueError:
            minDays = defaultDays
        try:
            minDist = int(self.request.query_params.get('distance', defaultDist))
        except ValueError:
            minDist = defaultDist

        collisionGraph = cache.get('featureGraph')
        featureSet = set()
        counter = 0
        for u, v, d in collisionGraph.edges(data=True):

            if d['daysApart'] <= minDays and d['distance'] <= minDist:
                featureSet = {u, v} | featureSet

        return featureSet
