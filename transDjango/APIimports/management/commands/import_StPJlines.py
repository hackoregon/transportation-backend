from django.core.management.base import BaseCommand, CommandError
from APIimports.models import StPJline
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
import os
import sys  



class Command(BaseCommand):
    help = 'Import Streets Permit Jobs lines'

    def handle(self, *args, **options):
        
        dataSet = DataSource(os.path.join(
            os.path.dirname(__file__),
            'datafiles',
            'Streets_Permit_Jobs_Line.geojson')
        )
        
        fieldMap = {
            'objectid' : 'OBJECTID',
            'linkpath' : 'LinkPath',
            'projectid' : 'ProjectID',
            'projectname' : 'ProjectName',
            'status' : 'Status',
            'contactname' : 'ContactName',
            'shape_length' : 'Shape_Length',
            'geom' : 'UNKNOWN',
        }

        lm = LayerMapping(StPJline, dataSet, fieldMap)
        lm.save()
