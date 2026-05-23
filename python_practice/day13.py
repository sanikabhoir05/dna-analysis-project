def calc(a,b):
    return a+b,a-b
s,d=calc(10,5)
print("Sum:",s)
print("difference:",d)

def student_marks(m1,m2):
    total=m1+m2
    average=total/2
    return total,average
t,avg=student_marks(80,90)
print("total:",t)
print("average:",avg)

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
print(add(10,20))
print(multiply(10,20))
print(subtract(10,20))

def get_marks():
    m1=int(input("enter marks 1:"))
    m2=int(input("enter marks 2:"))
    return m1,m2
def calculate(m1,m2):
    total=m1+m2
    avg=total/2
    return total,avg 
def display(total,avg):
    print("total:",total)
    print("average:",avg)
m1,m2=get_marks()
total,avg=calculate(m1,m2)
display(total,avg)

def multiply(a,b):
    return a+b,a-b
s,d=multiply(5,10)
print("sum:",s)
print("difference:",d)

def radius():
    m=int(input("enter number:"))
    return m
def calculate(m):
    result=3.14*m*m
    return result
def display(result):
    print("result:",result)
m=radius()
result=calculate(m)
display(result)

def large_number(a,b,c):
    if a>b>c:
        return a
    else:
        return c
a=int(input("Enter first number:"))
b=int(input("enter second number:"))
c=int(input("Enterr third number:"))
print("Larger number:",large_number(a,b,c))

def get_marks():
    m1=int(input("Enter marks 1:"))
    m2=int(input("Enter marks 2:"))
    m3=int(input("Enter marks 3:"))
    return m1,m2,m3
def calculate(m1,m2,m3):
    total=m1+m2+m3
    percentage=total/3
    return total,percentage
def grade_get(percentage):
    if percentage>=90:
        return"A"
    elif percentage>=70:
        return "B"
    else:
        return "Fail"
def display(total,percentage,grade):
    print("Total",total)
    print("Percentage",percentage)
    print("Grade:",grade)
m1,m2,m3=get_marks()
total,percentage=calculate(m1,m2,m3)
grade=grade_get(percentage)
display(total,percentage,grade)