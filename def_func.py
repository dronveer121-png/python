# # defining a func
# def avg(a,b,c):
#     print((a+b+c)/3)
# avg(2, 4, 2)

def avg(a,b,c):
    d = (a+b+c)/3
    return d #if use print(d) we acnnot assign value to o1

o1=avg(2,2,2)
print(o1) #nothing will be printed to print we need to use return

def greet(name):
    return f"hello {name}"
print(greet("allice"))


def add(a,b):
    return a+b
o1=add(2,3)
print(o1)

def stud(name,age):
    return f"my name is {name} and age is {age}"

o2=stud("dron",19)
print(o2)

# lamda function
square= lambda x,y:x+y
print(square(5,5))
# it is equal to 
def sum(x,y):
    return x+y
print(sum(4,5))

tri= lambda a,b:a*b*0.5
print(tri(4,5))
# same as
def tri(a,b):
    return a*b*0.5
