dna_sequences=["ATGC","CGT","TTA"]
print(dna_sequences[0])

dna_sequences=["ATG","CGT","CCC","GGG","ATG"]
print(dna_sequences[0])
print(dna_sequences[3])

genes=["BRCA1","TP53"]
genes.append("EGPR")
genes.remove("TP53")
genes.sort()
print(genes)

data=[
    ["BRCA1",1000],
    ["TP53",1200]
]
print(data[0])
print(data[0][1])

data=[
    ["BRCA1",1000],
    ["TP53",1200]
]
print(data[0][1])
print(data[1][1])

codon=("AUG","UUU","GGG")
print(codon[0])

dna={
    "A":5,
    "T":3,
    "U":2,
    "C":1
}
print(dna["A"])

dna="ATGC"
count={
    "A":0,
    "T":0,
    "G":0,
    "C":0
}
for base in dna:
    count[base]+=1
print(count)

dna="ATGCATGCATGC"
count={
    "A":0,
    "T":0,
    "G":0,
    "C":0
}
for base in dna:
    if base in count:
        count[base]+=1
print(count)



















