from django.db import models
from .modelDefinitions.CIPpoint import *
from .modelDefinitions.CIPline import *
from .modelDefinitions.StPJline import *

from django.contrib.postgres import fields as pg_fields
import django.utils.timezone


class ApiElement(models.Model):
    # The actual object represented by the api
    payload = pg_fields.JSONField()
    queryTime = models.DateTimeField(default=django.utils.timezone.now)
    url = models.CharField(max_length=2083)
    name = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Point(models.Model):
    geom = models.PointField()
    dateRange = models.CharField(max_length=1000, default=None)
    sourceRef = models.ForeignKey(ApiElement, default=None)
    data = models.TextField(default=None)
