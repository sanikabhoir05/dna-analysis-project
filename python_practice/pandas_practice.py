import pandas as pd
numbers= pd.Series([10,20,30,40])
print(numbers)

import pandas as pd
students={
    "Name":["A","B","C"],
    "Age":[18,19,20]
}
df=pd.DataFrame(students)
print(df)

import pandas as pd 
fruits={
    "Fruits":["Apple","Mango","Banana"],
    "Price":[100,80,50]
}
df=pd.DataFrame(fruits)
print(df)

import pandas as pd
no=pd.Series([5,10,15,20,25])
print(no)

import pandas as pd 
result={
    "Subject":["Biology","Chemistry","Maths"],
    "Marks":[88,75,92]
}
df=pd.DataFrame(result)
print(df)

import pandas as pd 
school={
    "Name":["Sanika","Saiesh"],
    "Age":[21,11]
}
df=pd.DataFrame(school)
print(df)