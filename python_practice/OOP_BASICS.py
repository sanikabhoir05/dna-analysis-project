class Student:
    def __init__(self, name):
        self.name=name
student1 = Student("Sanudi")
print(student1.name)

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
book1=Book("Python","John")
print(book1.title)
print(book1.author)

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
phone=Mobile("Samsung",2500000)
print(phone.brand)
print(phone.price)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print(self.name)
        print(self.salary)
emp=Employee("Amit",50000)
emp.details()

class Protien:
    def __init__(self,name,lenght):
        self.name=name
        self.lenght=lenght
protien=Protien("Haemoglobin",574)
print(protien.name)
print(protien.lenght)

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def details(self):
        print(self.name)
        print(self.age)
        print(self.marks)
stud=Student("SAnika",21,9.5)
stud.details()

class Gene:
    def __init__(self,gene_name,chromosome,expression_value):
        self.gene_name=gene_name
        self.chromosome=chromosome
        self.expression_value=expression_value
    def gene_detail(self):
        print("Gene_name",self.gene_name)
        print("Chromosome",self.chromosome)
        print("Expression_value",self.expression_value)
        print()
gene1=Gene("BRCA1","Chromosome17",52.4)
gene2=Gene("TP53","Chromosome17",30.8)
gene3=Gene("EFGR","Chromosome7",67.1)
gene1.gene_detail()
gene2.gene_detail()
gene3.gene_detail()

class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def make_sound(self):
        print(self.name,"says",self.sound)
Animal1=Animal("cat","meow")
Animal2=Animal("dog","woof")
Animal1.make_sound()
Animal2.make_sound()

class Protien:
    def __init__(self,protien_name,aa_lenght):
        self.protien_name=protien_name
        self.aa_lenght=aa_lenght
    def display(self):
        print("Protien",self.protien_name)
        print("Amino Acid",self.aa_lenght)
        print()
detail=Protien("Albumin",609)
detail.display()

class DnaSequence:
    def __init__(self,sequence):
        self.sequence=sequence
    def display(self):
        print("DNA sequence:",self.sequence)
dna1=DnaSequence("ATGCGTA")
dna1.display()

class DNASequence:
    def __init__(self,sequence):
        self.sequence=sequence
    def display(self):
        print("DNA Sequence:",self.sequence)
dna1=DNASequence("ATGCATGC")
dna2=DNASequence("CGTACTG")
dna1.display()
dna2.display()

class DNASequence:
    def __init__(self,sample,sequence):
        self.sample=sample
        self.sequence=sequence
    def display(self):
        print("Sample:",self.sample)
        print("Sequence:",self.sequence)
dna1=DNASequence("Patient_A","ATGCGT")
dna1.display()

class DNASeqeunce:
    def __init__(self,sample,species,seqeunce):
        self.sample=sample
        self.species=species
        self.seqeunce=seqeunce
    def display(self):
        print("Sample:",self.sample)
        print("Species:",self.species)
        print("DNA:",self.seqeunce)
dna1=DNASeqeunce(
    "Patient A",
    "Homo Sapeins",
    "ATGCGTC"
)
dna1.display()

class Stores:
    def __init__(self,sample_ID,Gene_Name,DNA_Seq):
        self.sample_ID=sample_ID
        self.Gene_Name=Gene_Name
        self.DNA_Seq=DNA_Seq
    def display(self):
        print("SAMPLE ID:",self.sample_ID)
        print("GENE NAME:",self.Gene_Name)
        print("DNA SEQ:",self.DNA_Seq)
dna1=Stores(
    "S101",
    "BRCA1",
    "ATGCGTACG"
)
dna1.display()

class Objects:
    def __init__(self,sequence):
        self.sequence=sequence
    def display(self):
        print(self.sequence)
seq1=Objects("ATGCGTA")
seq2=Objects("CGATCGA")
seq3=Objects("TTAACCG")
seq1.display()
seq2.display()
seq3.display()

class Lenght:
    def __init__(self,sample,seq):
        self.sample=sample
        self.seq=seq
    def display(self):
        lenght=len(self.seq)
        print("Sample:",self.sample)
        print("Seq:",self.seq)
        print("Lenght:",lenght)
patient1=Lenght(
    "Patient_A",
    "ATGCGTACGA",
)
patient1.display()