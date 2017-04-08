from django.core.management.base import BaseCommand, CommandError
from APIimports.importers.ingest_csv import csvToGeoJson
import csv
import json
#import datetime


class Command(BaseCommand):
    help = 'Ingest Data from saved and geocoded CSVs. Converts CSV to geojson.'

    def handle(self, *args, **options):
        apiList = [
            'Geocoded Data - Grind and Pave',
        ]

        csvToGeoJson(apiList)



