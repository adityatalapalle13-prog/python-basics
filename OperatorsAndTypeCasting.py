#Operators
#typecasting
#user input

print(15+5)
print(15-5)
print(15/5)
print(15*5)
print(15%6)#gives remainder
print(15//6)#gives only the integer value of the division
print(3**5)# 3 power 5

#TYPECASTING: conversion of one datatype into another
a="1"
b="2"
print(int(a)+int(b))
'''explicit conversion: done via programmer, done using functions int(),str(),hex(),float(),oct()
 implicit: done via python interpreter '''

c=3
d=4.78
print(c+d) #example for implicit, here it converted c from int type to float type

#USER INPUT
n=input("enter your name: ")
print("My name is", n)
x=input("enter a number: ")#Whatever you enter as an input it will take as a string datatype unless you mention the datatype
y=input("enter another number: ")
print(x+y)
print(int(x)+int(y))
p=int(input("enter a number: "))
q=int(input("enter another number: "))
print(p+q)