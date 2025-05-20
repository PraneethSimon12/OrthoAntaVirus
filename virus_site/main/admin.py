

from django.contrib import admin
from .models import VirusRecord

@admin.register(VirusRecord)
class VirusAdmin(admin.ModelAdmin):
    list_display = ('accession', 'organism_name', 'genbank_refseq', 'assembly', 'submitter', 'organization')
    search_fields = ('accession', 'organism_name', 'genbank_refseq', 'assembly', 'submitter', 'organization')