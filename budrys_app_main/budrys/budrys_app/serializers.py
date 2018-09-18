from .models import Animals
from rest_framework import serializers


class AnimalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animals
        fields = ("name",
                  "species",
                  "race",
                  "sex",
                  "age",
                  "weight",
                  "sterilized_castrated",
                  "description",
                  "image",
                  "img_main",
                  "img_main_alt",
                  "img_s",
                  "location",
                  "url",
                  "evidence_number",
                  "admission_date")
