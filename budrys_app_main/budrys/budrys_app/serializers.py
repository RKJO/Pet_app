from .models import Animals, Location
from rest_framework import serializers


class AnimalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animals
        fields = ("id",
                  "name",
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


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ("id",
                  "name",
                  "description",
                  "address",
                  "latitude",
                  "longitude",
                  "animals_count")

    animals_count = serializers.SerializerMethodField()

    def get_animals_count(self, obj):
        if not hasattr(obj, "animals_count") or obj.animals_count is None:
            return 0
        return obj.animals_count
