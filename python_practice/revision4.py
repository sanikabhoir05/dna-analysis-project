def sequence_lenght(seq):
    return len(seq)
dna="ATGCGTAAC"
print(sequence_lenght(dna))

def gc_content(seq):
    g=seq.count("G")
    c=seq.count("C")
    gc=((g+c)/len(seq))*100
    return gc
dna="ATGCCGTAAC"
print(gc_content(dna))
print(round(gc_content(dna),2))