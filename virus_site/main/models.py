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
        return self.organism_name
