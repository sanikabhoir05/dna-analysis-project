def hello():
    print("Hello Sanudi")
hello()
 
def greet(name):
    print("Hello",name)
greet("Sanudi")

def college(name):
    print("My college name is",name)
college("wilfred")

def DNA(base):
    print("BASE is",base)
DNA("ATGC")

def add(a,b):
    return a+b
x=add(2,3)
print(x)

def square(a):
    return a*a
x=square(12)
print(x)

def multiply(a,b):
    return a*b
x=multiply(7,5)
print(x)

def reverse_complement(dna):
    complement=""
    for base in dna:
        if base=="A":
            complement+="T"
        elif base=="T":
            complement+="A"
        elif base=="G":
            complement+="C"
        elif base=="C":
            complement+="G"
    reverse=complement[::-1]
    return reverse
result=reverse_complement("ATGC")
print(result)

def reverse_complement(dna):
    dna=dna.upper()
    complement=""
    for base in dna:
        if base=="A":
            complement+="T"
        elif base=="T":
            complement+="A"
        elif base=="G":
            complement+="C"
        elif base=="C":
            complement+="G"
        else:
            return"Invalid DNA"
    reverse=complement[::-1]
    return reverse
sequence=input("Enter dna sequence:")
result=reverse_complement(sequence)
print("Reverse Complement:",result)