file=open("new.txt","w")
file.write("Hello Bioinformatics\n")
file.write("Python")
file.close()

file=open("new.txt","r")
data=file.read()
print(data)
file.close()