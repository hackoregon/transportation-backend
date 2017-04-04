from django.core.management.base import BaseCommand
from APIimports.buildNetwork import getAllDateDistances

class Command(BaseCommand):
    help = 'Pre-build as much as possible for the conflict views'

    def handle(self, *args, **options):
        getAllDateDistances()