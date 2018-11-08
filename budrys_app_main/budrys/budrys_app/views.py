from django.core.paginator import Paginator
from django.db.models import Count
from django.template.response import TemplateResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from budrys_app.models import Animals, Location
from budrys_app.serializers import AnimalsSerializer, LocationSerializer


class AnimalsFilter(FilterSet):
    min_age = NumberFilter(field_name='age', lookup_expr='gte')
    max_age = NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = Animals
        fields = ('species', 'race', 'sex',  'age', 'weight', 'location')


class AnimalsListView(ListCreateAPIView):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalsFilter
    pagination_class = PageNumberPagination


class CountAnimalView(APIView):

    def get(self, request):
        pass


class AnimalsDetailView(View):

    def get(self, request, pk):
        animal = Animals.objects.get(pk=pk)
        ctx = {"animal": animal}
        return TemplateResponse(request, "animal_details.html", ctx)


class LocationListView(ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.annotate(animals_count=Count("animals")).all()


class LocationDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.annotate(animals_count=Count("animals")).all()
