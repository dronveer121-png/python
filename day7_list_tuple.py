a=5
table=[]
for i in range(1,11):
    table.append(a*i)
print(table)
# similar to

table1=[5*i for i in range (1,11)]
print(table1)

# tuple
a=(1,2,3,4)
x,y,z,q=a
print(y,x,z,q)