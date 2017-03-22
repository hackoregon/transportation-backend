from django.core.management.base import BaseCommand, CommandError
from APIimports.importers.ingest_geojson import jsonToPLP


class Command(BaseCommand):
    help = 'Ingest Data from saved GeoJsons'

    def handle(self, *args, **options):
        apiList = [
            'Capital Improv. Project - Points',
            'Capital Improv. Project - Lines',
            'Capital Improv. Project - Polygons',
            'Street Permit Jobs - Points',
            'Street Permit Jobs - Lines',
            'Street Permit Jobs - Polygons',
        ]

        jsonToPLP(apiList)
