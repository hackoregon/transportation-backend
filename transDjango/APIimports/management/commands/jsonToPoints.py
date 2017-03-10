from django.core.management.base import BaseCommand, CommandError
from APIimports.importers.import_points import jsonToPoints


class Command(BaseCommand):
    help = 'Import CIP points'

    def handle(self, *args, **options):
        apiList = ['Capital Improv. Project - Points']
        jsonToPoints(apiList)
