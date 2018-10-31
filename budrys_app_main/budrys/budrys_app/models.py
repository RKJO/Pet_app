from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date


class AddAndCreate(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_username(self):
        return self.created_at, self.created_at

    class Meta:
        abstract = True


class Location(AddAndCreate):
    name = models.CharField(max_length=120, null=True)
    description = models.TextField()
    address = models.CharField(max_length=120)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Animals(AddAndCreate):
    name = models.CharField(max_length=64)
    species = models.CharField(max_length=64, null=True)
    race = models.CharField(max_length=64, null=True)
    sex = models.CharField(max_length=64, null=True)
    age = models.IntegerField(null=True)
    weight = models.CharField(max_length=64, null=True)
    sterilized_castrated = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/', default='img/None/no-img.jpg')
    img_main = models.CharField(max_length=240, null=True)
    img_main_alt = models.CharField(max_length=240, null=True)
    img_s = ArrayField(
            models.CharField(max_length=250, null=True),
            size=8, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField()
    evidence_number = models.CharField(max_length=120, null=True)
    admission_date = models.DateField(default=date.today)


