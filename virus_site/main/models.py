from django.db import models

# Create your models here.

class VirusRecord(models.Model):
    accession = models.CharField(max_length=50)
    organism_name = models.CharField(max_length=100)
    genbank_refseq = models.CharField(max_length=50)
    assembly = models.CharField(max_length=50)
    submitter = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.accession} - {self.organism_name}"
    


class ImportVirusRecord(models.Model):
    accession_no = models.CharField(max_length=100)
    organism_name = models.CharField(max_length=200)
    vrl = models.CharField(max_length=50, blank=True, null=True)
    isolate = models.CharField(max_length=200, blank=True, null=True)
    species = models.CharField(max_length=200)
    length = models.IntegerField()
    geo_location = models.CharField(max_length=200, blank=True, null=True)
    host = models.CharField(max_length=200, blank=True, null=True)
    collection_date = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.organism_name

