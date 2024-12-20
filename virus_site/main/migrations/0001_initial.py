# Generated by Django 5.1.2 on 2024-10-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VirusRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.CharField(max_length=50)),
                ('organism_name', models.CharField(max_length=100)),
                ('genbank_refseq', models.CharField(max_length=50)),
                ('assembly', models.CharField(max_length=50)),
                ('submitter', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
            ],
        ),
    ]
