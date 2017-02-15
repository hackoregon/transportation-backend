from django.contrib.gis.db import models
#from .modelDefinitions.CIPpoint import *
#from .modelDefinitions.CIPline import *
#from .modelDefinitions.StPJline import *
from django.contrib.postgres.fields import DateRangeField


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
    dateRange = DateRangeField()
    sourceRef = models.ForeignKey(ApiElement, default=None)
    data = models.TextField(default=None)
