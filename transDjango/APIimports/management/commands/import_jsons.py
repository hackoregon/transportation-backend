from django.core.management.base import BaseCommand, CommandError
from APIimports.get_data import oneRingToBindThem
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
import os
import sys



class Command(BaseCommand):
    help = 'One ring to rule them all'

    def handle(self, *args, **options):
        oneRingToBindThem()






