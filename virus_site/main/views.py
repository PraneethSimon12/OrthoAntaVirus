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

# def upload_excel(request):
#     """Reads an Excel file and imports virus records into the database"""
    
#     # Check if the file exists
#     if not os.path.exists(EXCEL_FILE_PATH):
#         messages.error(request, f"⚠️ File not found: {EXCEL_FILE_PATH}")
#         print(f"❌ ERROR: File not found at {EXCEL_FILE_PATH}")
#         return redirect('virus_list')

#     try:
#         # ✅ Load the Excel file
#         df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')

#         # ✅ Print actual column headers for debugging
#         print("📢 DEBUG: Column Headers in Excel ->", df.columns.tolist())

#         # ✅ Standardize column names by stripping spaces
#         df.columns = df.columns.str.strip()

#         # ✅ Expected Columns (Updated to match ALL CAPS)
#         expected_columns = ["ACCESSION NO.", "ORGANISM NAME", "VRL", "ISOLATE", 
#                             "SPECIES", "LENGTH", "GEO LOCATION", "HOST", "COLLECTION DATE"]

#         # ✅ Check if all required columns exist
#         missing_columns = [col for col in expected_columns if col not in df.columns]
#         if missing_columns:
#             messages.error(request, f"⚠️ Missing columns in Excel: {missing_columns}")
#             print(f"❌ ERROR: Missing columns -> {missing_columns}")
#             return redirect('virus_list')

#         # ✅ Keep only the expected columns
#         df = df[expected_columns]

#         # ✅ Replace "not defined" with None for NULL values
#         df.replace("not defined", None, inplace=True)

#         # ✅ Convert "LENGTH" column to integer safely
#         df['LENGTH'] = pd.to_numeric(df['LENGTH'], errors='coerce').fillna(0).astype(int)

#         # ✅ Convert Dates to YYYY-MM-DD format
#         def format_date(value):
#             try:
#                 return pd.to_datetime(value, errors='coerce').strftime('%Y-%m-%d')
#             except:
#                 return None  # If invalid, store as NULL

#         df['COLLECTION DATE'] = df['COLLECTION DATE'].apply(format_date)
#         df['VRL'] = df['VRL'].apply(format_date)

#         # ✅ Insert data into the database
#         for _, row in df.iterrows():
#             ImportVirusRecord.objects.update_or_create(
#                 accession_no=row['ACCESSION NO.'],
#                 defaults={
#                     'organism_name': row['ORGANISM NAME'],
#                     'vrl': row['VRL'],
#                     'isolate': row['ISOLATE'],
#                     'species': row['SPECIES'],
#                     'length': row['LENGTH'],
#                     'geo_location': row['GEO LOCATION'],
#                     'host': row['HOST'],
#                     'collection_date': row['COLLECTION DATE']
#                 }
#             )
        
#         messages.success(request, "✅ Data imported successfully from RDRP_ORTHOHANTA.xlsx!")

#     except Exception as e:
#         messages.error(request, f"⚠️ Error importing data: {e}")
#         print(f"❌ ERROR: {e}")

#     return redirect('virus_list')

def upload_excel(request):
    """Handles file uploads, updates database, and paginates the records."""
    
    # Handle file upload
    if request.method == 'POST' and request.FILES.get('excel_file'):
        uploaded_file = request.FILES['excel_file']
        file_path = os.path.join("C:\\OrthoAntaVirus\\Database", uploaded_file.name)

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        messages.success(request, f"✅ File {uploaded_file.name} uploaded successfully!")
        return redirect('upload_excel')

    # Update the database before fetching records
    update_database_from_excel()

    # Fetch all virus records from the database
    records = ImportVirusRecord.objects.all().order_by('id')

    # Pagination (50 records per page)
    paginator = Paginator(records, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/upload_excel.html', {'records': page_obj})

def update_database_from_excel():
    """Reads the Excel file, updates the database, and removes missing rows"""
    if not os.path.exists(EXCEL_FILE_PATH):
        print(f"❌ ERROR: File not found at {EXCEL_FILE_PATH}")
        return

    try:
        df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')

        # ✅ Standardize column names (all caps, remove spaces)
        df.columns = df.columns.str.strip()

        expected_columns = ["ACCESSION NO.", "ORGANISM NAME", "VRL", "ISOLATE", 
                            "SPECIES", "LENGTH", "GEO LOCATION", "HOST", "COLLECTION DATE"]

        # ✅ Ensure the required columns exist
        missing_columns = [col for col in expected_columns if col not in df.columns]
        if missing_columns:
            print(f"❌ ERROR: Missing columns -> {missing_columns}")
            return

        df = df[expected_columns]
        df.replace("not defined", None, inplace=True)

        # ✅ Convert "LENGTH" column to integer safely
        df['LENGTH'] = pd.to_numeric(df['LENGTH'], errors='coerce').fillna(0).astype(int)

        # ✅ Convert Dates to YYYY-MM-DD format
        def format_date(value):
            try:
                return pd.to_datetime(value, errors='coerce').strftime('%Y-%m-%d')
            except:
                return None  # If invalid, store as NULL

        df['COLLECTION DATE'] = df['COLLECTION DATE'].apply(format_date)
        df['VRL'] = df['VRL'].apply(format_date)

        # ✅ Store only valid accession numbers from Excel
        excel_accession_numbers = df["ACCESSION NO."].dropna().astype(str).tolist()

        # ✅ Remove records that are in the database but missing from Excel
        ImportVirusRecord.objects.exclude(accession_no__in=excel_accession_numbers).delete()

        # ✅ Insert or update records from Excel
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

        print("✅ Database updated from Excel successfully (deleted missing records)!")

    except Exception as e:
        print(f"❌ ERROR: {e}")


def virus_list(request):
    """Fetches the latest virus records from the database and ensures it updates from Excel"""
    update_database_from_excel()  # ✅ Auto-update before fetching data
    records = ImportVirusRecord.objects.all()
    return render(request, 'main/virus_list.html', {'records': records})
