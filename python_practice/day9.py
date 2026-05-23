student={
    "name":"sanika",
    "marks":85
}
print(student["marks"])

student["age"]=20
student["marks"]=90
print(student)

data={
    "A":5,
    "T":3,
    "G":2
}
print(data.keys())
print(data.values())

dna="ATGCCTGA"
count={
    "A":0,
    "T":0,
    "G":0,
    "C":0,
}
for base in dna:
    count[base]+=1
print(count)


word="banana"
count={
    "b":0,
    "a":0,
    "n":0
}
for letters in word:
    count[letters]+=1
print(count)

dna="AATCGGTA"
count={
    "A":0,
    "T":0,
    "G":0,
    "C":0
}
for base in dna:
    count[base]+=1
print(count)

fruits={
    "apple":2,
    "banana":5
}
fruits["mango"]=3
fruits["banana"]=10
print(fruits)

person={
    "name":"sanika",
    "age":"20",
    "city":"mummbai"
}
print(person["name"])
print(person["age"])
print(person["city"])