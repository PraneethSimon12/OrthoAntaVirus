import openpyxl
from django.core.management.base import BaseCommand
from main.models import VirusRecord

class Command(BaseCommand):
    help = 'Load data from Excel file into the database'

    def handle(self, *args, **kwargs):
        workbook = openpyxl.load_workbook('data.xlsx')
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip the header
            VirusRecord.objects.create(
                accession=row[0],
                organism_name=row[1],
                genbank_refseq=row[2],
                assembly=row[3],
                submitter=row[4],
                organization=row[5]
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
