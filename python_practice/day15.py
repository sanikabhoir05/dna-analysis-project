def is_valid(seq):
    for i in seq:
        if i not in "ATGC":
            return False
        return True
def main():
    seq=input("Enter DNA seq:").upper()
    if not is_valid(seq):
        print("Invalid dna seq:")
        return
    lenght=len(seq)
    A=seq.count("A")
    T=seq.count("T")
    G=seq.count("G")
    C=seq.count("C")
    gc=((G+C)/lenght)*100
    at=((A+T)/lenght*100)
    print("Lenght",lenght)
    print("A:",A,"T:",T,"G:",G,"C:",C)
    print("GC%",gc)
    print("AT%",at)
main()
def clean_seqeunce(seq):
    return seq.upper()
seq=input("Enter Dna sequence:")
seq=clean_seqeunce(seq)
def nucloetide_percentage(seq):
    lenght=len(seq)
    A=seq.count("A")*100
    T=seq.count("T")*100
    G=seq.count("G")*100
    C=seq.count("C")*100
    return A,T,G,C
A_per,T_per,G_per,C_per=nucloetide_percentage(seq)
print("A%",A_per)
print("T%",T_per)
print("G%",G_per)
print("C%",C_per)
while True:
    seq=input("Enter seq")
    if seq.lower()=="exit":
        print("Program end")
        break
    seq=seq.lower()
    print("Length",len(seq))
def detect_type(seq):
    if "U" in seq:
        return "RNA"
    elif "T" in seq:
        return "DNA"
    else:
        return "Unknown"


