# Creating temporary files
t1=$(mktemp)
t2=$(mktemp)

# Contacts and genes paths
ContactsFile='merged_before_rna1.tsv'
GenesFile='genes1.tsv'

# Intersection of contacts and genes, strands are stored in corresponding files; didn't find bedtools on HPC-2 so provided thast files
bedtools intersect -a <(cat $ContactsFile| awk '{print $2, $3, $4}'  OFS='\t') -b <(cat $GenesFile) -wb > intersected_genes.tsv
bedtools intersect -a <(cat $ContactsFile| awk '{print $2, $3, $4, $5, $1}'  OFS='\t') -b <(cat $GenesFile) -wa > intersected_contacts.tsv

# Counting how many contacts intersected certain gene = gene score
cat intersected_genes.tsv | awk '{print $9}' | sort | uniq -c > gene_score.csv

# Adding score column to the intersection from the genes perspective
join -1 9 -2 2 -o1.1,1.2,1.3,1.7,1.8,1.9,1.10,2.1 <(sort -k 9,9 intersected_genes.tsv) gene_score.csv > intersected_scored_genes.csv

# Dividing by gene length
cat intersected_scored_genes.csv | awk '{print $1,$2,$3,$4,$5,$6,$7,$8,$8/$7}' > intersected_scored_genes_divided.csv

# Joining intersections based on chr-begin-end-strand concatenated column
join -j1 -o1.2,1.3,1.4,1.5,1.6,1.7,1.10,2.6 <(<intersected_scored_genes_divided.csv awk '{print $1"-"$2"-"$3"-"$4" "$0}' | sort -k1,1 | uniq) <(<intersected_contacts.tsv awk '{print $1"-"$2"-"$3"-"$4" "$0}' | sort -k1,1 | uniq) > joined_annotation.csv

# Voting for the most contacted gene: sorting by contact id then by gene score and filttering all annotations but the one with the highest score
sort -k8,8 -k7nr,7 joined_annotation.csv | uniq -f7 > unique_annotation.csv

# Adding leading zeroes; can be avoided by sorting stringwise, not numberwise
# cat unique_annotation.csv | awk  '{ a=sprintf("%09d",$8); print a, $0}' OFS='\t' > unique_annotation2.csv
# cat $ContactsFile | awk  '{ $1=sprintf("%09d",$1); print $0}' OFS='\t' | sort -k1n,1 > ${ContactsFile}2

# Assigning annotation to the initial contacts
cat unique_annotation.csv > $t1
cat $ContactsFile | sort -k1,1 > $t2
join -1 8 -2 1  -o2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,2.10,2.11,1.5,1.6,1.7,1.8 $t1 $t2 > annotated_contacts.csv

# Deleting temporary files
rm -f $t1 $t2
