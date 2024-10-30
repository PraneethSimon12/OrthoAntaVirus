from django.shortcuts import render

# Create your views here.

from .models import VirusRecord

def virus_list(request):
    viruses = VirusRecord.objects.all()
    return render(request, 'ncbi/virus_list.html', {'viruses': viruses})

