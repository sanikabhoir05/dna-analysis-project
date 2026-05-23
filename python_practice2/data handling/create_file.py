file=open("notes.txt","w")
file.write("I am learning python\n")
file.write("Bioinformatics")
file.close()

file=open("notes.txt","r")
data=file.read()
print(data)
file.close


