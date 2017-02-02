from django.db import models


from .modelDefinitions.CIPpoint import *


from django.contrib.postgres import fields as pg_fields

class ApiElement(models.Model):
    # The actual object represented by the api
    payload = pg_fields.JSONField()
    queryTime = models.DateTimeField()
    url = models.CharField(max_length=2083)

class Project(models.Model):
    geom = models.MultiPointField()
    bureau = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    period = pg_fields.DateRangeField()
    original = models.ForeignKey(ApiElement)
