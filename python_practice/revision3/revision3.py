radius=float(input("Enter radius:"))
area=3.14*radius*radius
print("Area=",area)

c=float(input("Enter Calcius:"))
f=(c*9/5)+32
print("Fahrenheit=",f)

num=int(input("Enter number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")

dna=input("Enter Dna:")
print("Lenght:",len(dna))
print("First base:",dna[0])
print("Last base:",[-1])

dna=input("Enter Dna:")
if len(dna)>100:
    print("Long Sequence")
else:
    print("Short sequence")

base=input("Enter base:")
if base=="A" or base=="T" or base=="G" or base=="C":
    print("valid base")
else:
    print("invalid base")

dna=input("Enter dna:")
a=t=g=c=0
for base in dna:
    if base=="A":
        a+=1
    elif base=="T":
        t+=1
    elif base=="G":
        g+=1
    elif base=="C":
        c+=1
print("A=",a)
print("T=",t)
print("G=",g)
print("C=",c)

dna=input("Enter Dna:")
rev=""
for base in dna:
    rev=base+rev
print("Reversed=",rev)

dna=input("Enter DNA")
for base in dna:
    print(base)

while True:
    dna=input("Enter dna:")
    if dna=="stop":
        print("program stopped")
        break

count=0
while True:
    dna=input("Enter dna:")
    if dna=="stop":
        break
    count+=1
print("Total sequence:",count)

dna=input("Enter dna:")
g=c=0
for base in dna:
    if dna=="G":
        g+=1
    elif dna=="C":
        c+=1
gc=((g+c)/len(dna))*100
print("GC content=",gc)