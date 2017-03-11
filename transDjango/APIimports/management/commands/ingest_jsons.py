from django.core.management.base import BaseCommand, CommandError
from APIimports.importers.import_points import jsonToPoints


class Command(BaseCommand):
    help = 'Import CIP points'

    def handle(self, *args, **options):
        apiList = [
            'Capital Improv. Project - Points',
            'Capital Improv. Project - Lines',
            'Capital Improv. Project - Polygons',
            'Street Permit Jobs - Points',
            'Street Permit Jobs - Lines',
            'Street Permit Jobs - Polygons',
        ]

        jsonToPoints(apiList)
