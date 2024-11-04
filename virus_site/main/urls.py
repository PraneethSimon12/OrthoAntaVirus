from django.urls import path

from . import views

urlpatterns = [
    path('', views.virus_list, name='virus_list'),
    path('index', views.index, name='index'),
]