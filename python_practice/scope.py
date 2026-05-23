def hello():
    name="Sanudi"
    print(name)
hello()

name="sanudi"
def hello():
    print(name)
hello()
print(name)

x=10
def test():
    x=5
    print(x)
test()
print(x)

x=10
def test():
    global x
    x=50
test()
print(x)

x=20
def demo():
    x=5
    print("Inside:",x)
demo()
print("outside:",x)

score=10
def increase():
    global score 
    score+=5
increase()
print("Final score:",score)

toy="Car"
def show_toy():
    print("Toy is",toy)
show_toy()

def secret_toy():
    toy="Robot"
    print("Inside function:",toy)
secret_toy()
print("outside function:",toy)

score=50
def increase_score():
    global score
    score+=10
increase_score()
print("Final score",score)

def maths(a,b):
    return a+b
x=maths(2,3)
print(x)

name="sani"
def change():
    global name
    name="Python"
change()
print(name)
