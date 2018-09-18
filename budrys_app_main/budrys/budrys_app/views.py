from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from budrys_app.models import Animals
from budrys_app.serializers import AnimalsSerializer


class AnimalsListView(ListCreateAPIView):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()


class AnimalsDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalsSerializer
    queryset = Animals.objects.all()


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
