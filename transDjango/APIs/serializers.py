from APIimports.models import Feature, API_element
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers


class FeatureSerializer(gis_serializers.GeoFeatureModelSerializer):
    
    class Meta:
        model = Feature
        geo_field = 'geom'
        fields = ['id', 'canonical_daterange', 'data', 'source_name', 'canonical_status']
        abstract = True

