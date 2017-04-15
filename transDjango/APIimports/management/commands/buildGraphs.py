from django.core.management.base import BaseCommand
from APIimports.buildGraphs import buildGraphs


class Command(BaseCommand):
    help = 'Pre-build as much as possible for the conflict views'

    def handle(self, *args, **options):
        buildGraphs()
