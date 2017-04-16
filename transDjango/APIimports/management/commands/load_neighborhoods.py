from django.core.management.base import BaseCommand, CommandError
from APIimports.importers.load_neighborhoods import load_neighborhoods


class Command(BaseCommand):
    help = 'Import neighborhood polygons directly into its own table'

    def handle(self, *args, **options):
        load_neighborhoods()