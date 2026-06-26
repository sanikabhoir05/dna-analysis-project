def sequence_lenght(seq):
    return len(seq)
def gc_content(seq):
    g=seq.count("G")
    c=seq.count("C")
    gc=(g+c)/len(seq)*100
    return gc
def reverse_sequence(seq):
    return seq[::-1]
def nucleotide_count(seq):
    return{
        "A":seq.count("A"),
        "T":seq.count("T"),
        "G":seq.count("G"),
        "C":seq.count("C")
    }
dna=input("Enter dna sequence:")
print(sequence_lenght(dna))
print(gc_content(dna))
print(reverse_sequence(dna))
counts=nucleotide_count(dna)
for key,value in counts.items():
    print(key,"=",value)


