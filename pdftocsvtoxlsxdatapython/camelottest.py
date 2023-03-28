import camelot
import os
import pandas as pd
# PDF file to extract tables from
pdf_folder = 'GUJARATI/'
paths = [pdf_folder + fn for fn in os.listdir(pdf_folder) if fn.endswith('.pdf')]

for path in paths:
    filename = path.replace('pdf', 'csv')
    tables = camelot.read_pdf("/Users/apple/Downloads/pdfdatapython/GUJARATI/15-Magnesium-rich-veg-recipes-Gujarati.pdf", pages = "all", encoding='utf-8')
    df_p4 = tables[0].df
    print('df',df_p4)
    # print('path',path,filename)
    # tables = camelot.read_pdf("/Users/apple/Downloads/pdfdatapython/GUJARATI/15-Magnesium-rich-veg-recipes-Gujarati.pdf", pages='all', flavor='stream')
    # for table in tables:
    #     print(table.df)
    # the following lines seem to be duplicate
    #tables.export(filename, f='csv', compress=True) # json, excel, html, sqlite
    #tables.to_csv(filename)