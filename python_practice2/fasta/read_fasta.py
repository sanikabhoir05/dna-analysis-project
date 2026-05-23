file=open("python_practice2/fasta/dna.fasta","r")
for line in file:
    if not line.startswith(">"):
        print(line.strip())
file.close()

file=open("python_practice2/fasta/dna.fasta","r")
sequence=""
for line in file:
    if not line.startswith(">"):
        sequence+=line.strip()
print(sequence)
file.close()

file=open("python_practice2/fasta/dna.fasta","r")
data=file.read()
print(data)
file.close()

file=open("python_practice2/fasta/dna.fasta","r")
sequence={}
header=""
for line in file:
    head=line[1:]
else:
    sequence[header]=line
for name in sequence:
    print(name)
file.close()
for name, seq in sequence.items():
    print("Sequences name:", name)
    print("Sequences:",seq)
    print("Lenght:",len(seq))
    print("A count:", seq.count("A"))
    print("T count:",seq.count("T"))
    print("G count:",seq.count("G"))
    print("C count:",seq.count("C"))
    print()

gc_count=seq.count("G") + seq.count("C")
print("GC_Count",gc_count)

file=open("python_practice2/fasta/dna.fasta","r")
sequences={}
longest_name=""
longest_seq=""
for name,seq in sequences.items():
    if len(seq)>len(longest_seq):
        longest_seq=seq
        longest_name=name
print("Longest seq belongs to:",longest_name)
print("Sequences:",longest_seq)
print("lenght:",len(longest_seq))

file=open("python_practice2/fasta/dna.fasta","r")
sequences={}
name=""
for line in file:
    line=line.strip()
    if line.startswith(">"):
        name=line[1:]
        sequences[name]=""
    else:
        sequences[name]+=line
file.close()
longest_name=""
longest_seq=""
for name,seq in sequences.items():
    if len(seq)>len(longest_seq):
        longest_seq=seq
        longest_name=name
print("Longest seq belongs to:",longest_name)
print("Sequences:",longest_seq)
print("Length:",len(longest_seq))