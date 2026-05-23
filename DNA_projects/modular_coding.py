def count_bases(dna):
    print("A:",dna.count("A"))
    print("T:",dna.count("T"))
    print("G:",dna.count("G"))
    print("C:",dna.count("C"))

def dna_length(dna):
    print("Length:",len(dna))

def reverse_dna(dna):
    print("Reverse:",dna[::-1])

def dna_to_rna_(dna):
    print("RNA:",dna.replace("T","U"))

def clean_dna(dna):
    return dna.upper()

def has_mutation(dna):
    if "AAA" in dna:
        print("mutation found")
    else:
        print("no mutation")
    
def gc_content(dna):
    g=dna.count("G")
    c=dna.count("C")
    total=len(dna)
    gc=((g+c)/total)*100
    print("GC content:",gc)

def starts_with_start_codon(dna):
    if dna.startswith("ATG"):
        print("Protein coding sequence ")
    else:
        print("Not protein coding")

def repeat_sequence(dna,times):
    print(dna*times)

def validate_dna(dna):
    valid_bases = "ATGC"
    for letter in dna:
        if letter not in valid_bases:
            print("Invalid DNA")
            return
    print("Valid DNA")

def split_codons(dna):
    for i in range(0, len(dna), 3):
        print(dna[i:i*3])

dna=input("Enter dna sequence:")
times=int(input("Enter repeat number:"))

count_bases(dna)
dna_length(dna)
reverse_dna(dna)
dna_to_rna_(dna)
clean_dna(dna)
has_mutation(dna)
gc_content(dna)
starts_with_start_codon(dna)
repeat_sequence(dna,times)
validate_dna(dna)
split_codons(dna)