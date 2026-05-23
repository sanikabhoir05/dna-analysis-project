try:
    a=int(input("enter number:"))
    print(10/a)
except ZeroDivisionError:
    print("something went wrong")
except ValueError:
    print("enter valid number")

try:
    num=int(input("Enter a number:"))
    result=100/num
    print("Result:",result)
except ZeroDivisionError:
    print("you entered zero!")
except ValueError:
    print("invalid input!")

def add(a,b):
    return a+b
x=int(input("enter a number"))
y=int(input("Enter a number:"))
print("result",add(x,y))

try:
   def square(a):
       return a*a
   x=int(input("enter a number:"))
   print("result:",square(x))
except ZeroDivisionError:
   print("you entered zero!")

try:
    def multiplication(a,b):
        return a/b
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))
    print("result:",multiplication(x/y))
except ZeroDivisionError:
    print("you entered zero!")
except ValueError:
    print("enter invalid number!")
 
def calc(a,b):
    return a/b
num1=int(input("Enter:"))
num2=int(input("Enter:"))
print("result",calc(num1/num2))

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a-b
def divide(a,b):
    return a/b
print("Choose operation")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
try:
    choice=int(input("enter choice(1-4)"))
    num1=float(input("enter first number"))
    num2=float(input("enter second number"))
    if choice==1:
        print("result:",add(num1,num2))
    elif choice==2:
        print("result:",subtract(num1,num2))
    elif choice==3:
        print("result:",multiply(num1,num2))
    elif choice==4:
        print("result:",multiply(num1,num2))
    else:
        print("reult invalid")
except ZeroDivisionError:
    print("cannot divide by zero!")
except ValueError:
    print("invalid value!")
