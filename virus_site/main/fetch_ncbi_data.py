from Bio import Entrez
import pandas as pd

def fetch_ncbi_data():
    Entrez.email = "praneethsimon2004@gmail.com"
    Entrez.api_key = "9831e23b87f6ab5095ca4985da457db42808"

    search_term = "Orthohantavirus[Organism]"
    handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=500)
    record = Entrez.read(handle)
    handle.close()

    ids = record["IdList"]
    print(f"🔍 Found {len(ids)} records")

    virus_data = []
    for i in range(0, len(ids), 20):
        batch = ids[i:i+20]
        handle = Entrez.efetch(db="nucleotide", id=batch, rettype="gb", retmode="text")
        data = handle.read()
        handle.close()

        for entry in data.split("\n\n"):
            lines = entry.split("\n")
            result = {"Accession": None, "Organism": None, "Length": None}
            for line in lines:
                if line.startswith("ACCESSION"):
                    result["Accession"] = line.split()[1]
                if "ORGANISM" in line:
                    result["Organism"] = line.strip().split("ORGANISM")[-1].strip()
                if line.startswith("LOCUS"):
                    try:
                        result["Length"] = int(line.split()[2])
                    except:
                        result["Length"] = None
            virus_data.append(result)

    df = pd.DataFrame(virus_data)
    df.to_excel("Orthohantavirus_Data.xlsx", index=False)
    print("✅ Saved to Orthohantavirus_Data.xlsx")
