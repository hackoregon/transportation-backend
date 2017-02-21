from APIimports.models import Point, Line, ApiElement
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers


class PointSerializer(gis_serializers.GeoFeatureModelSerializer):
    sourceRef = serializers.StringRelatedField()

    class Meta:
        model = Point
        geo_field = 'geom'
        fields = ['dateRange', 'data', 'sourceRef']
        abstract = True


class LineSerializer(PointSerializer):

    class Meta(PointSerializer.Meta):
        model = Line
