from django.db import models
from datetime import date


class Animals(models.Model):
    name = models.CharField(max_length=64)
    species = models.CharField(max_length=64)
    race = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    age = models.DateField(null=True)
    weight = models.IntegerField(null=True)
    sterilized_castrated = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/', default='img/None/no-img.jpg')
    img_main = models.CharField(max_length=240, null=True)
    img_main_alt = models.CharField(max_length=240, null=True)
    img_s = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=120)
    url = models.URLField()
    evidence_number = models.CharField(max_length=120, null=True)
    admission_date = models.DateField(default=date.today)