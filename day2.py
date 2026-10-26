# # typecasting = making varibles of one data type into another data type
# a="10"
# b="4"
# print(int(a)+int(b))

# # user input
# a= input("enter your name:")
# print(a)
# x= input("enter value of x:")
# y=input("enetr value of y:")
# print(x+y)
# print(int(x)+int(y))

# strings 

#  for multi line code string use ''' '''
a='''hi mm a python developer
nice to meet you'''
print(a)
print(a[3])#to access a particular character in string

# using for loop to access each character in string
for x in a:
    print(x) 

#string slicing = for extracting a part of string
m="hello world"
print(m[0:5])

#string methods
# 1. upper() = converts string to uppercase 
# 2. lower() = converts string to lowercase
# 3. strip() = removes whitespace from the beginning and end of string
# 4. replace() = replaces a string with another string
# 5. split() = splits the string into a list of strings         
# 6. find() = finds a string in another string and returns the index of the first occurrence
# 7. count() = counts the number of occurrences of a string in another string diff from len
# 8. endswith() = returns True if the string ends with the specified value
# 8. discard() = wont give error if elemrnt is not present if present then will remove it
r="    im dronveer singh"
print(r.upper())
z=r.strip()
print(z)
print(r.find('singh'))
print(z.replace('im','hi'))
print(z.endswith('singh'))







    
    