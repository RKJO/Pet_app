from django.core.paginator import Paginator
from django.template.response import TemplateResponse
from django.views import View

from budrys_app.models import Animals


class AllAnimalsView(View):

    def get(self, request):
        animals_list = Animals.objects.all()
        paginator = Paginator(animals_list, 15)  # Show 25 contacts per page

        page = request.GET.get('page')
        allanimals = paginator.get_page(page)

        return TemplateResponse(request, 'animals_list_all.html', {
            'animals_list': allanimals
        })


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
#             students = Animals.objects.filter(last_name__icontains=phrase).order_by('last_name')
#             ctx.update({
#                 'student_list': students,
#                 'phrase': phrase,
#             })
#         return TemplateResponse(request, 'animal_search.html', ctx)
#
