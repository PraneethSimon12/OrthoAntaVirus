from django.shortcuts import render

# Create your views here.

from .models import VirusRecord



def index_view(request):
    return render(request, 'main/index.html') 

def page2_view(request):
    return render(request, 'main/page2.html')

def landing_page(request):
    return render(request, 'main/landingpage.html')