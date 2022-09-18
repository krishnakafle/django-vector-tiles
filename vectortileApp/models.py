# from django.db import models
from django.contrib.gis.db import models


class District(models.Model):
    gid = models.AutoField(primary_key=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    first_stat = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(srid=4326)
    
    class Meta:
        managed = False
        db_table = 'district'
