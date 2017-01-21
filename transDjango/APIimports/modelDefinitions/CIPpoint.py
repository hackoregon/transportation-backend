
from django.contrib.gis.db import models

# Create your models here.


class CIPpoint (models.Model):
    PrjNumSAP = models.CharField(max_length=1000, null=False, blank=False)
    PrjName = models.CharField(max_length=1000)
    Status = models.CharField(max_length=1000)
    Comments = models.CharField(max_length=1000)
    Program = models.CharField(max_length=1000)
    FundSrc = models.CharField(max_length=1000)
    EstCost = models.DecimalField(max_digits=12, decimal_places=2)
    Bureau = models.CharField(max_length=1000)
    Contact = models.CharField(max_length=1000)
    Geom = models.MultiPointField()

    def __str__(self):
        return '{} - {}'.format(self.PrjNumSAP, self.PrjName)
