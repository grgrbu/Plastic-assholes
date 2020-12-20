import sys
from Bio import Entrez

Entrez.email = "X@Y.com"

accessions = []
with open(sys.argv[1], "r") as accession_numbers:
    for accession_number in accession_numbers:
        accession_number = accession_number.strip()
        accessions.append(accession_number)

ids = ','.join(accessions)
with open(sys.argv[2], "w") as fasta:
    with Entrez.efetch(db="protein", id=ids, rettype="fasta") as handle:
        fasta.write(handle.read())
