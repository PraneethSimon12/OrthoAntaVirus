import os
import pandas as pd
from django.core.management.base import BaseCommand
from main.models import VirusRecord

class Command(BaseCommand):
    help = 'Import Excel files into the VirusRecord model'

    def handle(self, *args, **kwargs):
        folder_path = 'C:\OrthoAntaVirus\Database'  # Update with the path to your Excel files

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                file_path = os.path.join(folder_path, file_name)
                df = pd.read_excel(file_path)

                for _, row in df.iterrows():
                    VirusRecord.objects.create(
                        accession=row['Accession'],
                        organism_name=row['Organism Name'],
                        genbank_refseq=row['GenBank/RefSeq'],
                        assembly=row['Assembly'],
                        submitter=row['Submitter'],
                        organization=row['Organization']
                    )
                self.stdout.write(f'Imported {file_name}')

        self.stdout.write('All files imported successfully.')
