import pandas as pd
from sys import argv

dna = pd.read_csv(argv[1], sep = "\t", header = None)
rna = pd.read_csv(argv[2], sep = "\t", header = None)
dna.set_index([3], inplace=True)
rna.set_index([3], inplace=True)
ids = list(set(dna.index) & set(rna.index))                  
dna = dna.loc[ids,]
rna = rna.loc[ids,]
res = pd.DataFrame(index=range(len(ids)),\
columns=['id', 'rna_chr', 'rna_bgn', 'rna_end', 'rna_strand', 'rna_cigar',\
'dna_chr', 'dna_bgn', 'dna_end', 'dna_strand', 'dna_cigar'])
for i, item in enumerate(ids):
    res.at[i,'id'] = item
    res.at[i,'rna_chr'] = rna.at[item,0]
    res.at[i,'rna_bgn'] = rna.at[item,1]
    res.at[i,'rna_end'] = rna.at[item,2]
    res.at[i,'rna_strand'] = rna.at[item,5]
    res.at[i,'rna_cigar'] = rna.at[item,6]
    res.at[i,'dna_chr'] = dna.at[item,0]
    res.at[i,'dna_bgn'] = dna.at[item,1]
    res.at[i,'dna_end'] = dna.at[item,2]
    res.at[i,'dna_strand'] = dna.at[item,5]
    res.at[i,'dna_cigar'] = dna.at[item,6]
res.to_csv(argv[3], sep='\t', index=False, header=True)