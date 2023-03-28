import tabula

# Read pdf into list of DataFrame
#dfs = tabula.read_pdf("timescript sample/sft-wfh-boys-p-2-5.pdf", pages='all')

# convert PDF into CSV file
tabula.convert_into("/Users/apple/Downloads/pdfdatapython/For NN _ extraction_Q1 2021.pdf", "/Users/apple/Downloads/pdfdatapython/For NN _ extraction_Q1 2021.csv", output_format="csv", pages='all')