from django.shortcuts import render

# Create your views here.

from .models import VirusRecord

def virus_list(request):
    viruses = VirusRecord.objects.all()
    return render(request, 'main/virus_list.html', {'viruses': viruses})

def index(request):
    return render(request, 'main/index.html') 

def page2_view(request):
    return render(request, 'main/page2.html')