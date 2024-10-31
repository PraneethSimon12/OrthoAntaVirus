from django.urls import path

from . import views

urlpatterns = [
    path('', views.virus_list, name='virus_list'),
]