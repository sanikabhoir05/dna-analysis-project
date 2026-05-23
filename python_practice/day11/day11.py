def say_hello():
    print("Hello sani")
say_hello()

def greet(name):
    print("Hello",name)
greet("sanika")
greet("Rahul")

def add(a,b):
    return a+b
result=add(5,3)
print(result)

def square(num):
    return num*num
print(square(4))
print(square(3))

def multiply(x,y):
    return x*y
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("Result",multiply(x,y))

def says_welcome():
    print("Sanika")
says_welcome()

def cube(num):
    return num*num*num
x=int(input("Enter a number:"))
result=cube(x)
print("cube is",cube)

def get_marks(grades):
    if grades >=90:
        return"A"
    elif grades >=70:
        return "B"
    elif grades >=50:
        return "C"
    else:
        return"fail"
x=int(input("Enter marks:"))
marks=get_marks(x)
print("Marks",marks)

def get_larger(a,b):
    if a>b:
        return a
    else:
        return b
x=(int(input("enter first number:")))
y=int(input("enter second number:"))
print("larger number is:",get_larger(x,y))