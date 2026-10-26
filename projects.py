#project 1 = calculator

# a= int(input("enter first no."))
# b= int(input("enter 2nd no."))

# print("add",a+b)
# print("subtract",a-b)
# print("multi",a*b)
# print("divide", a/b)

# loops

# a=int(input("enter a no."))

# if (a>0):
#     print("no. is positive")
# elif (a<0):
#     print("no. is negative")
# else:
#     print("no. is zero")

# b= int(input("enter the age"))
# if b>=18 :
#     print("can drive")
# else:
#     print("cannot drive")

# c=int(input("enter a no."))
# if c%2==0 :
#     print("no.is even")
# else:
#     print("no. is odd")



     
# a=int(input("enter a no."))
# match a:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _ :
#         print("invalid")


# x= int(input("enter no. 1 "))
# y= int(input("enter no. 2 "))
# z= int(input("enter operation "))
# match z :
#     case 1:
#         print(x+y)
#     case 2:
#         print(x-y)
#     case 3:
#         print(x*y)
#     case 4:
#         print(x/y)


# total = 0 #important
# for i in range(1,101):
#     print(i)
#     total += i

# print(total)


# for i in range(0,6):
#     print("*"*i)    

# for i in range(5,0,-1):
#      print("*"*i)


# i=1
# while i<=10:
#  print(i)
#  i=i+1

# password="dron"
# a=(input("enter password  "))
# while (a!=password):
#     a=input("wrong try again")
# print("correct")


# i=1
# sum=0
# while i<101:
#     print(i)
#     i=i+1
#     sum=sum+i
# print(sum)

# i=str(input("enter the no."))
# while i:
#     print(i[::-1])
#     break



 # for i in range(0,11):
#     if(i==6):
#      continue
#     print(i)

# name="dronveer"
# print(name[0:1])
# print(name[7:])
# print(len(name))


# a="hello","world"
# print(" ".join(a))

# text="python programming"
# print(text[0:6])
# print(text[0::2])
# print(text[::-1])

# string="  i love python programming  "
# print(string.strip())
# print(string.upper())
# print(string.count("o"))

# a="asd"
# print(a.isalnum())

# print("my name is {} and im {}".format("john","25"))

# name="john"
# age="25"
# print(f"my name is {name} and my age is {age}")

# sen="coding in python is fun"
# print(sen.replace("python","c++").replace("fun","sad"))
# print(sen.find("python"))

# a=input("write a sentence=")
# vow="aeiou"
# count=0
# for i in a:
#     if i in vow:
#         count+=1
# print(count)

# print(a.count(["a","e","i","o","u"]))  IT IS WRONG AND CANNOT BE DONE

# a=input("enter a word")      
# b=a[::-1]
# if a==b:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome121")

# '''fibonacci'''#recursion

# def fib(n):
#     if n==0 or n==1:
#      return n

#     return fib(n-2) + fib(n-1)

# print(fib(3))



# def greet():
#    print("im a student")
# greet()

# def sqr(a):
#    print("square is =",a*a)
# sqr(5)

# def stu(name,age):
#    return f"{name} {age}"
# print(stu("dron",19))

# def area(a,b=10):
#     c=a*b
#     return c
# print(area(5))

# sum= lambda a,b:a+b
# print(sum(2,5))

# def factorial(n):
#    if n==0 or n==1:
#     return 1
#    return factorial(n-1)*n
# print(factorial(5))

# def sum(n):
#    if n==0:
#     return 0
#    return n%10 + sum(n//10)
# print(sum(1234)) 

        
# fruits=["apple","banana","cherry"]
# fruits[1]="orange"
# print(fruits)

list1 =[i for i in range (1,11)]
print(list1)
print(list1[0:3])
print(list1[-3:])

