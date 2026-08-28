from ete3 import NCBITaxa
ncbi = NCBITaxa()
result = ncbi.get_name_translator(["Arthropoda"])
print(result)
