from APIimports.models import Point
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers


class PointSerializer(gis_serializers.GeoFeatureModelSerializer):


    class Meta:
        model = Point
        geo_field = 'geom'

        fields = ['dateRange', 'data', 'sourceRef']
