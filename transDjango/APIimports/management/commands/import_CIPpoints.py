from django.core.management.base import BaseCommand, CommandError
from APIimports.models import CIPpoint
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
import os
import sys  



class Command(BaseCommand):
    help = 'Import CIP points'

    # def add_arguments(self, parser):
    #     parser.add_argument('filePath', metavar='geojson file')

    def handle(self, *args, **options):
        
        dataSet = DataSource(os.path.join(
            os.path.dirname(__file__),
            'datafiles',
            'Capital_Improvement_Projects_CIP_Points.geojson')
        )
        #layer = dataSet[0]
        #print('\n'.join(layer.fields))
        
        fieldMap = {
            'PrjNumSAP': 'Project_Number_SAP',
            'PrjName': 'Project_Name',
            'Status': 'Status',
            'Comments': 'Comments',
            'Program': 'Program',
            'FundSrc': 'Funding_Source',
            'EstCost': 'Estimated_Total_Project_Cost',
            'Bureau': 'Bureau_Name',
            'Contact': 'Contact',
            'Geom': 'POINT',
        }

        lm = LayerMapping(CIPpoint, dataSet, fieldMap)
        lm.save()

       


        