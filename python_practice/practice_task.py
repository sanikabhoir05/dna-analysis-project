class DNASequence:
    def __init__(self,sequence):
        self.sequence=sequence
    def gc_content(self):
        gc=self.sequence.count("G")+self.sequence.count("C")
        lenght=len(self.sequence)
        if lenght==0:
            return 0
        return(gc/lenght)*100
    def display(self):
        print("DNA Sequence:",self.sequence)
        print("Lenght:",len(self.sequence))
        print("GC content:{:.2f}%".format(self.gc_content()))
seq=input("Enter DNA Sequence:")
dna=DNASequence(seq)
dna.display()

class DNASequence:
    def __init__(self,seq):
        self.seq=seq.upper()
    def gc_content(self):
        gc=self.seq.count("G")+self.seq.count("C")
        lenght=len(self.seq)
        if lenght==0:
            return 0
        return(gc/lenght)*100
    def reverse_seq(self):
        return self.seq[::-1]
    def complement(self):
        mapping={
            "A":"T",
            "T":"A",
            "G":"C",
            "C":"C"
        }
        return self.complement
    def display(self): 
       at=self.seq.count("A")+self.seq.count("T")
       at=self.seq.count("G")+self.seq.count("C")
       print("A Count:",self.seq.count("A"))
       print("A Count:",self.seq.count("T"))
       print("A Count:",self.seq.count("G"))
       print("A Count:",self.seq.count("C"))
       print("DNA seqeunce:",self.seq())
       print("Lenght:",len(self.seq))
       print("A/T Count:",at)
       print("G/C Count:",gc)
       print("GC Content:{:.2f}%".format(self.gc_content()))
       print("reverse seqeunce",self.reverse_seq())
       print("Complement:",self,self.complement())
    seq=input("Enter DNA seq:")
    dna=DNASequence(seq)
    dna.display()
    
    