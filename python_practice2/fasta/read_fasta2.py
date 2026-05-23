file=open("python_practice2/fasta/dna.fasta2","r")
sequences=[]
for line in file:
    if not line.startswith(">"):
        sequences.append(line.strip())
print(sequences)
file.close()

file=open("python_practice2/fasta/dna.fasta2","r")
sequences={}
for line in file:
    line=line.strip()
    if line.startswith(">"):
        header=line[1:]
    else:
        sequences[header]=line
print(sequences)
file.close()

file=open("python_practice2/fasta/dna.fasta2")
sequences=[]
for line in file:
    if not line.startswith(">"):
        sequences+=line.strip()
print(sequences)
file.close()

file=open("python_practice2/fasta/dna.fasta2")
sequences={}
header=""
for line in file:
    line=line.strip()
    if line.startswith(">"):
        header=line[1:]
    else:
        sequences[header]=line
print(sequences["Dog"])
file.close()

file=open("python_practice2/fasta/dna.fasta2")
sequences=[]
for line in file:
    if not line.startswith(">"):
        sequences.append(line.strip())
print("Total sequences:",len(sequences))
file.close()

file=open("python_practice2/fasta/dna.fasta2")
sequences={}
header=""
for line in file:
    line=line.strip()
    if line.startswith(">"):
        header=line[1:]
    else:
        sequences[header]=line
for name,seq in sequences.items():
    print(name,len(seq))
file.close()