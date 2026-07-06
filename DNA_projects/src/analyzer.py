import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df=pd.read_csv(r"C:\python programs\DNA_projects\data\data.csv")
print("Dataset")
print(df)
print("\nSummary")
print(df.describe())
mean=np.mean(df["Expression"])
median=np.median(df["Expression"])
maximum=np.max(df["Expression"])
minimum=np.min(df["Expression"])
print("\nStatistics")
print("Mean:",mean)
print("Median:",median)
print("Maximum:",maximum)
print("Minimum:",minimum)
plt.bar(df["Gene"],df["Expression"])
plt.title("Gene Expression")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.show()
for index,row in df.iterrows():
    if row["Expression"]>15:
        print (row["Gene"],"->Highly Expressed")
    else:
        print(row["Gene"],"->Normal")


    