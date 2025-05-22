from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.

from .models import VirusRecord
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ImportVirusRecord
from django.core.files.storage import FileSystemStorage
import os



def index_view(request):
    return render(request, 'main/index.html') 


def page2_view(request):
    return render(request, 'main/page2.html')

def landing_page(request):
    """Renders the landing page for Orthohantavirus Resource."""
    countries = [
        "Argentina", "Australia", "Austria", "Belgium", "Benin", "Bolivia", "Brazil", "Canada",
        "Chile", "China", "Colombia", "Croatia", "Czech Republic", "Denmark", "Ethiopia",
        "Finland", "France", "French Guiana", "Germany", "Greece", "Guinea", "Honduras",
        "Hungary", "Indonesia", "Italy", "Japan", "Kazakhstan", "Latvia", "Lithuania",
        "Madagascar", "Malaysia", "Mexico", "Mongolia", "Netherlands", "North Korea",
        "Panama", "Paraguay", "Peru", "Poland", "Russia", "Singapore", "Slovakia", "Slovenia",
        "South Korea", "Spain", "Sri Lanka", "Sweden", "Switzerland", "Taiwan", "Thailand",
        "Turkey", "United Kingdom", "USA", "Venezuela", "Vietnam", "Others"
    ]

    return render(request, "main/landingpage.html", {"countries": countries})

EXCEL_FILE_PATH = r"C:\OrthoAntaVirus\Database\RDRP_ORTHOHANTA.xlsx"


def update_database_from_excel():
    """Update DB from Excel - your existing logic here"""
    if not os.path.exists(EXCEL_FILE_PATH):
        print(f"File not found at {EXCEL_FILE_PATH}")
        return

    try:
        df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')
        df.columns = df.columns.str.strip()

        expected_columns = ["ACCESSION NO.", "ORGANISM NAME", "VRL", "ISOLATE",
                            "SPECIES", "LENGTH", "GEO LOCATION", "HOST", "COLLECTION DATE"]

        missing_cols = [col for col in expected_columns if col not in df.columns]
        if missing_cols:
            print(f"Missing columns: {missing_cols}")
            return

        df = df[expected_columns]
        df.replace("not defined", None, inplace=True)
        df['LENGTH'] = pd.to_numeric(df['LENGTH'], errors='coerce').fillna(0).astype(int)

        def format_date(value):
            try:
                return pd.to_datetime(value, errors='coerce').strftime('%Y-%m-%d')
            except:
                return None

        df['COLLECTION DATE'] = df['COLLECTION DATE'].apply(format_date)
        df['VRL'] = df['VRL'].apply(format_date)

        excel_accessions = df["ACCESSION NO."].dropna().astype(str).tolist()
        ImportVirusRecord.objects.exclude(accession_no__in=excel_accessions).delete()

        for _, row in df.iterrows():
            ImportVirusRecord.objects.update_or_create(
                accession_no=row['ACCESSION NO.'],
                defaults={
                    'organism_name': row['ORGANISM NAME'],
                    'vrl': row['VRL'],
                    'isolate': row['ISOLATE'],
                    'species': row['SPECIES'],
                    'length': row['LENGTH'],
                    'geo_location': row['GEO LOCATION'],
                    'host': row['HOST'],
                    'collection_date': row['COLLECTION DATE']
                }
            )

        print("Database updated from Excel successfully!")

    except Exception as e:
        print(f"Error updating DB: {e}")


def upload_excel(request):
    # Handle file upload via POST
    if request.method == 'POST' and request.FILES.get('excel_file'):
        uploaded_file = request.FILES['excel_file']
        file_path = os.path.join("C:\\OrthoAntaVirus\\Database", uploaded_file.name)

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        messages.success(request, f"File {uploaded_file.name} uploaded successfully!")
        return redirect('upload_excel')

    # Update database before querying
    update_database_from_excel()

    # Get filter values from GET params
    sequence_type = request.GET.get('sequence_type')
    protein_type = request.GET.get('protein_type')
    keyword = request.GET.get('keyword', '').strip()
    accession_no = request.GET.get('accession_no', '').strip()
    species = request.GET.get('species', '').strip()
    country_region = request.GET.get('country_region', '').strip()
    host = request.GET.get('host', '').strip()
    length_min = request.GET.get('length_min')
    length_max = request.GET.get('length_max')
    collection_date = request.GET.get('collection_date')
    release_date = request.GET.get('release_date')

    # Start queryset
    records = ImportVirusRecord.objects.all()

    # Apply filters stepwise if provided
    if accession_no:
        records = records.filter(accession_no__icontains=accession_no)
    if keyword:
        records = records.filter(organism_name__icontains=keyword)
    if species:
        records = records.filter(species__icontains=species)
    if country_region:
        records = records.filter(geo_location__icontains=country_region)
    if host:
        records = records.filter(host__icontains=host)
    if length_min and length_min.isdigit():
        records = records.filter(length__gte=int(length_min))
    if length_max and length_max.isdigit():
        records = records.filter(length__lte=int(length_max))
    if collection_date:
        records = records.filter(collection_date=collection_date)
    # Note: Add release_date filtering if relevant field exists

    # If you want, filter by sequence_type or protein_type depending on your model/data structure

    records = records.order_by('id')

    # Paginate (50 per page)
    paginator = Paginator(records, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Render template with paginated filtered results
    return render(request, 'main/upload_excel.html', {
        'records': page_obj,
        'filters': request.GET,
    })


def virus_list(request):
    """Fetches the latest virus records from the database and ensures it updates from Excel"""
    update_database_from_excel()  # ✅ Auto-update before fetching data
    records = ImportVirusRecord.objects.all()
    return render(request, 'main/virus_list.html', {'records': records})

def home_view(request):
    return render(request, 'main/home.html')

def filter_view(request):
    return render(request, 'main/filter.html')