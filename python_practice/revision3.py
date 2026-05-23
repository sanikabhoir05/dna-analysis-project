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

def gc_at_content(seq):
    g=seq.count("G")
    c=seq.count("C")
    a=seq.count("A")
    t=seq.count("A")
    gc=((g+c)/len(seq))*100
    at=((a+t)/len(seq))*100
    return gc,at
dna="ATGGCTAT"
gc,at=gc_at_content(dna)
print("GC%",round(gc,2))
print("AT%",round(at,2))

def nucleotide_count(seq):
    return{
        "A":seq.count("A"),
        "T":seq.count("T"),
        "G":seq.count("G"),
        "C":seq.count("C")
    }
dna="ATGGCGT"
print(nucleotide_count(dna))

def gc_count(seq):
    try:
        g=seq.count("G")
        c=seq.count("C")
        return((g+c)/len(seq))*100
    except ZeroDivisionError:
        return "sequence is empty"
dna=""
print(gc_content(dna))

def dna_to_rna(seq):
    rna=seq.replace("T","U")
    return rna
dna+"ATGCCGT"
result=dna_to_rna(dna)
print("DNA",dna)
print("RNA",result)

