#MAP

cube=lambda x: x**3

l=[1,2,3,4,5,6,7,8,9]
l2=[]
for i in l:
    l2.append(cube(i))

print(l2)

#other way to do this is:

newl=map(cube,l)
print(newl)
newl=list(map(cube,l))
print(newl)

#FILTER

def filter_function(a):
    return a>4 # returns true or false

newl2=list(filter(filter_function,l))
print(newl2)

#REDUCE
from functools import reduce
list1=[1,2,3,4,5,6,7,8,9]
totalsum=reduce(lambda a,b:a+b,list1)
print(totalsum)