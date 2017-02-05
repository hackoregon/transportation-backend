
from django.contrib.gis.db import models

class StPJline(models.Model):
    objectid = models.IntegerField()
    linkpath = models.CharField(max_length=1000)
    projectid = models.CharField(max_length=1000)
    projectname = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    contactname = models.CharField(max_length=1000)
    shape_length = models.FloatField()
    geom = models.GeometryField()

    def __str__(self):
        return '{} - {}'.format(self.projectid, self.projectname)
