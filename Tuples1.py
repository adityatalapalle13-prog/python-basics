tup=(1,2,3,4,5,6,7,"green") #They are similar to lists, but these are non-iterable
print(type(tup))
print(tup)
tup2=(1,)#the comma is necessary for it to declare as tuple otherwise it would take it as an integer
print(type(tup2),tup2)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-2])

if "green" in tup:
    print("green is an element of tup")

tup3=tup[1:3] #unlike lists here tup won't change since tuples aren't iterable
print(tup3,"this is tup3")

#OPERATIONS OF TUPLES
# Tuple are immutable , hence if you want to add,remove or change tuple items, then first you must convert the tuples to a list
#Then perform operation on that list and convert it back to tuple

#example
countries=("India ","Russia","china","USA")

tempList2=list(countries)#here it's converted into list
tempList2.append("Italy")
tempList2.pop(3)   #removes the  element
countries=tuple(tempList2) #here it's converted into tuple
# we can concatenate tuples without converting them into list

#methods of tuples
print(countries.count("Russia"))#counts the number of times the element is repeated
print(countries.index("Russia"))#gives the index number of the first occurrence of the input  element
tuple21=(1,2,3,2,3,3,2,3,2)
print(tuple21.index(3,4,8)) #value:,start:,stop:
print(len(tuple21))

