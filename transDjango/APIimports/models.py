from django.contrib.gis.db import models
from django.contrib.postgres.fields import DateRangeField
from django.contrib.postgres import fields as pg_fields
import django.utils.timezone


class ApiElement(models.Model):
    # The actual object represented by the api
    payload = pg_fields.JSONField()
    queryTime = models.DateTimeField(default=django.utils.timezone.now)
    url = models.CharField(max_length=2083)
    apiName = models.CharField(max_length=2083)
    projectName = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Point(models.Model):
    geom = models.PointField()
    dateRange = DateRangeField()
    sourceRef = models.ForeignKey(ApiElement, default=None)
    data = models.TextField(default=None)


class Line(models.Model):
    geom = models.GeometryField()
    dateRange = DateRangeField()
    sourceRef = models.ForeignKey(ApiElement, default=None)
    data = models.TextField(default=None)


class Polygon(models.Model):
    geom = models.GeometryField()
    dateRange = DateRangeField()
    sourceRef = models.ForeignKey(ApiElement, default=None)
    data = models.TextField(default=None)