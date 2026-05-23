def greet(name="Student"):
    print("Hello",name)
greet("Sanika")
greet()

def greet(name="student"):
    print("Welcome",name)
greet("Sanika")
greet()

def my_func():
    x=10
    print(x)
my_func()

x=20
def my_func():
    print(x)
my_func()

a=5
def my_func():
    print(a)
my_func()

def my_func():
    a=10
    print(a)
my_func()

def gc_content(sequence):
    g=sequence.count("G")
    c=sequence.count("C")
    total=len(sequence)
    if total==0:
        return 0
    return (g+c)/total*100
dna="ATGCGCATA"
result=gc_content(dna)
print("GC%:",gc_content(dna))

def gc_content(sequence="ATGC"):
    g=sequence.count("G")
    c=sequence.count("C")
    total=len(sequence)
    if total==0:
        return 0
    return(g+c)/total*100
print(gc_content())
print(gc_content("ATGC"))

def gc_content(sequence):
    g=sequence.count("G")
    c=sequence.count("C")
    total=len(sequence)
    if total==0:
        return 0
    return(g+c)/total*100
dna=input("Enter dna:")
print("GC%:",gc_content(dna))

def gc_content(sequence):
    g=sequence.count("G")
    c=sequence.count("C")
    total=len(sequence)
    if total==0:
        return 0
    return(g+c)/total*100
dna=input("Enter dna:").upper()
print("GC%:",gc_content(dna))