sequence=input("enter dna sequence:").upper()
gc_count=0
at_count=0
i=0
while i<len(sequence):
    if sequence[i]=="G" or sequence[i]=="C":
        gc_count+=1
    elif sequence[i]=="A" or sequence[i]=="T":
        at_count+=1
    i+=1
gc_percent=(gc_count/len(sequence))*100
at_percent=(at_count/len(sequence))*100
print("DNA sequemce:",sequence)
print("total bases:",len(sequence))
print("GC_content:",round(gc_percent,2),"%2")
print("AT_content:",round(at_percent,2),"%2")
