from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date


class Location(models.Model):
    name = models.CharField(max_length=64, null=True)
    description = models.TextField()
    address = models.CharField(max_length=120)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Animals(models.Model):
    name = models.CharField(max_length=64)
    species = models.CharField(max_length=64)
    race = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    age = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    sterilized_castrated = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/', default='img/None/no-img.jpg')
    img_main = models.CharField(max_length=240, null=True)
    img_main_alt = models.CharField(max_length=240, null=True)
    img_s = ArrayField(
            models.CharField(max_length=250, blank=True),
            size=8)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField()
    evidence_number = models.CharField(max_length=120, null=True)
    admission_date = models.DateField(default=date.today)


