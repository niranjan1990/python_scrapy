import tabula
import os

#pdf_path = "timescript/Basics-of-newborn-care-English-timed.pdf"
pdf_folder = 'GUJARATI/'
paths = [pdf_folder + fn for fn in os.listdir(pdf_folder) if fn.endswith('.pdf')]

#dfs = tabula.read_pdf(pdf_path, stream=True)
for path in paths:
    print(path)
    filename = path.replace('pdf', 'csv')
    dfs = tabula.convert_into(path, filename,lattice=True, output_format="csv", pages='all')
# read_pdf returns list of DataFrames
#print(dfs)

