from django.core.management.base import BaseCommand
from APIimports.buildNetwork import getAllDateDistances

class Command(BaseCommand):
    help = 'One ring to rule them all'

    def handle(self, *args, **options):
        getAllDateDistances()