from django.contrib.gis.db import models
from django.contrib.postgres.fields import DateRangeField
from django.contrib.postgres import fields as pg_fields
import django.utils.timezone


class API_element(models.Model):
    # The actual object represented by the api
    payload = pg_fields.JSONField()
    query_time = models.DateTimeField(default=django.utils.timezone.now)
    url = models.CharField(max_length=2083)
    api_name = models.CharField(max_length=2083)
    source_name = models.CharField(max_length=2083)

    def __str__(self):
        return self.projectName


class Feature(models.Model):
    geom = models.GeometryField()
    orig_daterange = DateRangeField()
    canonical_daterange = DateRangeField()
    orig_status = models.CharField(max_length=2083)
    canonical_status = models.CharField(max_length=2083)
    source_ref = models.ForeignKey(API_element)
    source_name = models.CharField(max_length=2083)
    data = models.TextField(default=None)