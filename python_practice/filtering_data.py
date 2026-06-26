import pandas as pd 
data={
    "Name":["Rahul","Sneha","Amit","Pooja"],
    "Age":[19,20,21,22]
}
df=pd.DataFrame(data)
print(df["Name"])
print(df[df["Age"]>20])

import pandas as pd 
data={
    "Name":["Sanika","Saiesh","Jethalal","Tapu"],
    "Marks":[65,75,85,95]
}
df=pd.DataFrame(data)
print(df["Marks"])

import pandas as pd
data={
    "Name":["S","A","N","I","K","A"],
    "Age":[10,15,12,25,30,35]
}
df=pd.DataFrame(data)
print(df[df["Age"]>20])

import pandas as pd 
data={
    "Name":["S","A","N","I","K"],
    "City":["Pune","Mumbai","Ghatkopar","Panvel","Kamothe"],
    "Marks":[35,45,55,65,75]
}
df=pd.DataFrame(data)
print(df["Name"])
print(df[["Name","Marks"]])
print(df[df["Marks"]>80])
print(df[df["City"]=="Pune"])