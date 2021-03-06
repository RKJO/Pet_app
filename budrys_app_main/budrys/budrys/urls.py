"""budrys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from budrys_app import views
from budrys_app.views import AnimalsListView, AnimalsDetailView, LocationListView, LocationDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^animals/$', AnimalsListView.as_view(), name='animal-list'),
    url(r'^location/$', LocationListView.as_view(), name='location-list'),
    url(r'^animals/(?P<pk>[\d]+)/$', AnimalsDetailView.as_view(), name='animal-detail'),
    url(r'^location/(?P<pk>[\d]+)/$', LocationDetailView.as_view(), name='location-detail'),
    # path('', views.AllAnimalsView.as_view(), name="index"),
    # path('animsals/<int:pk>/', views.AnimalDetailView.as_view(), name="animal-detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)