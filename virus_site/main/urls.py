from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.virus_list, name='virus_list'),
#     path('index', views.index, name='index'),
# ]

urlpatterns = [
    path('', views.index_view, name='index'),  # Homepage
    path('page2/', views.page2_view, name='page2'),  # Page 2
    path('land/', views.landing_page, name='landing_page'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('virus_list/',views.virus_list, name='virus_list'),  # landing_page page
]


