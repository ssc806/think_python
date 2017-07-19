from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CameraLocaiton(models.Model):
    index = models.AutoField(primary_key=True)
    camera_id = models.IntegerField()
    address = models.CharField(max_length=256)
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)

    class Meta:
        ordering = ['-camera_id',]
        db_table = 'camera_location'
        managed = False
