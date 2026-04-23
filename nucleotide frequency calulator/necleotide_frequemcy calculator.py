dna=input("enter dna sequence:").upper()
freq={
    "A":0,
    "T":0,
    "G":0,
    "C":0
}
for base in dna:
    if base in freq:
        freq[base]+=1
print("NUcleotide Frequency:")
for key in freq:
    print(key,":",freq[key])

total=sum(freq.values())
print("\nPercentage")
for  key in freq:
    percent=(freq[key]/total)*100
    print(key,".",round(percent,2),"%")

invalid=0
for base in dna:
    if base in freq:
        freq[base]+=1
    else:
        invalid+=1
print("invalid characters:0",invalid)

if total>0:
    gc_content=((freq["G"]+freq["C"])/total)*100
print("GC Content:",round(gc_content,2),"%")

most_freq=max(freq,key=freq.get)
print("most freq nucleotides:",most_freq)