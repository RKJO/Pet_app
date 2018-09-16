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
    img_main = models.CharField(max_length=64, null=True)
    img_main_alt = models.CharField(max_length=64, null=True)
    img_s = models.CharField(max_length=64, null=True)
    location = models.CharField(max_length=120)
    url = models.URLField()
    evidence_number = models.CharField(max_length=64, null=True)
    admission_date = models.DateField(default=date.today)


#
# Animals.objects.create(
#     name="Budrys",
#     species="Pies",
#     race="mieszaniec",
#     sex="samiec",
#     age=2017-10,
#     weight=7,
#     sterilized_castrated="tak",
#     description="Wesoły pies, pełen energii",
#     img_main="https://source.unsplash.com/1600x900/?dog",
#     location="Kaliny Jedrusik 6 01-748 Warszawa",
#     url="https//source.unsplash.com/",
#     evidence_number="1")
#
#Animals.objects.create(
#     name="Budrys",
#     species="Pies",
#     race="mieszaniec",
#     sex="samiec",
#     age=2017-10,
#     weight=7,
#     sterilized_castrated="tak",
#     description="Franek dopiero co trafił do schroniska i wciąż się poznajemy, ale już dziś możemy powiedzieć, że Franek uwielbia towarzystwo człowieka i mimo tego, że został określony na ok.11 lat, to przy człowieku zachowuje się jak szczeniak! Upomina się o uwagę, skacze, prosi o przytulenie, pogłaskanie, wskakuje na kolana. Jest bardzo spragniony kontaktu z człowiekiem i strasznie prosi, żeby go samego nie zostawiać :( Franio mimo tego, że ma w sobie mnóstwo energii, jest już starszym pieskiem i szuka domu który zapewni mu nie tylko miłość, ale i dobrą opiekę weterynaryjną. Więcej informacji: Agnieszka 604 28 28 39, Dominika 609 464 592. Skąd: Warszawa, Łochowska (Praga Północ)",
#     img_main="https://source.unsplash.com/1600x900/?dog",
#     location="tatarska Warszawa",
#     url="https//source.unsplash.com/",
#     evidence_number="1")

#Animals.objects.create(
#   name="Lucky",
#   species="Pies",
#   race="mieszaniec",
#   sex="samiec",
#   age="2017-09-01",
#   weight=12,
#   sterilized_castrated="tak",
#   description="Wesoły pies, pełen energii",
#   img_main="https://source.unsplash.com/1600x900/?dog",
#   location="Kaliny Jedrusik 6 01-748 Warszawa",
#   url="https//source.unsplash.com/")

# Animals.objects.create(
#    name="Max",
#    species="Pies",
#    race="mieszaniec",
#    sex="samiec",
#    age="2017-09-01",
#    weight=18,
#    sterilized_castrated="tak",
#    description="Wesoły pies, pełen energii",
#    img_main="https://source.unsplash.com/1600x900/?dog",
#    location="przyokopowa 33 01-208 Warszawa",
#    url="https//source.unsplash.com/")
#
