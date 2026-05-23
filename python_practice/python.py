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
