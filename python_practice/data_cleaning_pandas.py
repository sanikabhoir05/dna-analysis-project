import pandas as pd
data={
    "Name":["A","B","C"],
    "Marks":[90,None,75]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())

import pandas as pd 
data={
    "Name":["A","B","C"],
    "Marks":[90,None,75]
}
df=pd.DataFrame(data)
df["Marks"]=df["Marks"].fillna(0)
print(df)

import pandas as pd 
data={
    "Name":["ravi","neha","karan"],
    "Marks":[88,None,95]
}
df=pd.DataFrame(data)
print(df.isnull().sum())
df["Marks"]=df["Marks"].fillna(0)
print(df)

import pandas as pd 
data={
    "Product":["Apple","Banana","Mango","orange"],
    "Price":[100,None,150,None]
}
df=pd.DataFrame(data)
print(df.isnull().sum())
df["Price"]=df["Price"].fillna(50)
print(df)

import pandas as pd
data={
    "Gene":["BRCA1","TP53","EFGR","MYC"],
    "Expression":[25,None,30,None]
}
df=pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum())
df["Expression"]=df["Expression"].fillna(0)
print(df)