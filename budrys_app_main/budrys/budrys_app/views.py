from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter

from budrys_app.models import Animals
from budrys_app.serializers import AnimalsSerializer


class AnimalsFilter(FilterSet):
    min_age = NumberFilter(field_name='age', lookup_expr='gte')
    max_age = NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = Animals
        fields = ('age',)

class AnimalsListView(ListCreateAPIView):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalsFilter

# class AnimalsDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AnimalsSerializer
#     queryset = Animals.objects.all()

class AnimalsDetailView(View):

    def get(self, request, pk):
        animal = Animals.objects.get(pk=pk)
        ctx = {
            "animal": animal,
             }

        return TemplateResponse(request, "animal_details.html", ctx)
