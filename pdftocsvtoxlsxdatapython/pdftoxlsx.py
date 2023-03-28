import glob
import tabula

# transform the pdfs into excel files
for filepath in glob.iglob('/Users/apple/Downloads/pdfdatapython/GUJARATI/*.pdf'):
    filename = filepath.replace('pdf', 'json')
    tabula.convert_into(filepath,filename,lattice=True, output_format="json",pages='all')


