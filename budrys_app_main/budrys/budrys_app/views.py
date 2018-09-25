from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from budrys_app.models import Animals
from budrys_app.serializers import AnimalsSerializer


class AnimalsListView(ListCreateAPIView):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()


# class AnimalsDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = AnimalsSerializer
#     queryset = Animals.objects.all()


class AnimalsDetailView(View):

    def get(self, request, pk):
        animal = Animals.objects.get(pk=pk)
        ctx = {
            "animal": animal,
            # "animal_name": animal.name,
            # "animal_species": animal.species,
            # "animal_race": animal.race,
            # "animal_sex": animal.sex,
            # "animal_age": animal.age,
            # "animal_weight": animal.weight,
            # "animal_sterilized_castrated": animal.sterilized_castrated,
            # "animal_description": animal.description,
            # "animal_image": animal.image,
            # "animal_img_main": animal.img_main,
            # "animal_img_main_alt": animal.img_main_alt,
            # "animal_img_s": animal.img_s,
            # "animal_url": animal.url,
             }

        return TemplateResponse(request, "animal_details.html", ctx)


# class AllAnimalsView(View):
#
#     def get(self, request):
#         animals_list = Animals.objects.all()
#         paginator = Paginator(animals_list, 15)  # Show 25 contacts per page
#
#         page = request.GET.get('page')
#         allanimals = paginator.get_page(page)
#
#         return TemplateResponse(request, 'animals_list_all.html', {
#             'animals_list': allanimals
#         })


# class AnimalSearchView(View):
#
#     def get(self, request):
#         return TemplateResponse(request, 'animal_search.html', {
#             "form": AnimalSearchForm()
#         })
#
#     def post(self, request):
#         form = AnimalSearchForm(data=request.POST)
#         ctx = {'form': form}
#         if form.is_valid():
#             phrase = form.cleaned_data['phrase']
#             animals = Animals.objects.filter(name__icontains=phrase).order_by('name')
#             ctx.update({
#                 'student_list': animals,
#                 'phrase': phrase,
#             })
#         return TemplateResponse(request, 'animal_search.html', ctx)
#
