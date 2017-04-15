from django.core.management.base import BaseCommand, CommandError
from APIimports.importers.ingest_geojson_local import load_local_json


class Command(BaseCommand):
    help = 'Ingest Data from converted City of Portland Shapefiles. Data should \
    be in geojson format.'

    def handle(self, *args, **options):
        apiList = [
            'ROW Closures',
        ]

        load_local_json(apiList)