#creating local variable into global variable
def sum(a,b):
    c=a+b
    global z #created a global variable    z=0
    return c

z=3
print(sum(2,3))
print(z)