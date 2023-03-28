import glob
import pandas as pd

excel_files = glob.glob('/Users/apple/Downloads/pdfdatapython/GUJARATI/') # assume the path
for excel in excel_files:
    out = excel.split('.')[0]+'.csv'
    df = pd.read_excel(excel) # if only the first sheet is needed.
    df.to_csv(out) 