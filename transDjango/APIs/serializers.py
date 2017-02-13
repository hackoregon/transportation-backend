from APIimports.models import Point
from rest_framework import serializers


class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        geo_field = 'geom'

        fields = ['dateRange']
