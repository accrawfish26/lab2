import pandas as pd

url = ("https://www.ncbi.nlm.nih.gov/geo/download/"
       "?acc=GSE52778&format=file&file=GSE52778_All_Sample_FPKM_Matrix.txt.gz")
fpkm = pd.read_csv(url, sep="\t", compression="gzip")

print(fpkm.head())
