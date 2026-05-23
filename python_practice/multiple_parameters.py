def student(name,age):
    print(name)
    print(age)
student("Sanika",20)

def calc(a,b):
    sum=a+b
    product=a*b
    return sum,product
x,y=calc(2,3)
print(x)
print(y)

def dna_lenght(sequence):
    return len(sequence)
dna="ATGC"
lenght=dna_lenght(dna)
print("Lenght:",lenght)

def gc_count(sequence):
    g=sequence.count("G")
    c=sequence.count("C")
    return g,c
dna="GCGCTA"
g_count,c_count=gc_count(dna)
print("G:",g_count)
print("C:",c_count)

def gc_percentage(sequence):
    g=sequence.count("G")
    c=sequence.count("C")
    total=len(sequence)
    gc=((g+c)/total)*100
    return gc 
dna="GCGCTA"
answer=gc_percentage(dna)
print("GC Percentage:",answer)

def gc_counts(sequence):
    a=sequence.count("A")
    return a 
dna="AAAAT"
a_count=gc_counts(dna)
print("A:",a_count)

def dna_data(sequence):
    lenght=len(sequence)
    t_count=sequence.count("T")
    return lenght,t_count 
dna="ATGC"
lenght,t_count=dna_data(dna)
print("Lenght:",lenght)
print("T count:",t_count)

def dna_info(sequence):
    lenght=len(sequence)
    g=sequence.count("G")
    c=sequence.count("C")
    gc=((g+c)/lenght)*100
    return lenght, round(gc,2)
dna=input("enter dna:")
lenght, gc_percent=dna_info(dna)
print("Lenght:",lenght)
print("GC%",gc_percent)

def gc_percentage(sequence):
    lenght=len(sequence)
    g=sequence.count("G")
    c=sequence.count("C")
    gc=((g+c)/lenght)*100
    return lenght, round(gc,2)
dna=input("Enter lenght:")
lenght, gc_percent=gc_percentage(dna)
print("lenght:",lenght)
print("GC%",gc_percent)