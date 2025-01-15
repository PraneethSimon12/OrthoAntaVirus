from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.virus_list, name='virus_list'),
#     path('index', views.index, name='index'),
# ]

urlpatterns = [
    path('', views.index_view, name='index'),  # Homepage
    path('page2/', views.page2_view, name='page2'),  # Page 2
    path('land/', views.landing_page, name='landing_page'),  # landing_page page
]