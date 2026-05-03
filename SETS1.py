#Sets are unordered collection of data items,Sets are unchangeable, and they do not contain duplicate items
s={2,3,True,False,"hey",False}
print(s)#you can see that they do not maintain order,so we cannot use something like s.index

g={}
print(type(g))#since we use curly brackets for dictionary as well, you cannot create empty set like this

h=set()
print(type(h))

#SETS METHODS
s={1,2,5,6}
s1={3,6,7}
print(s1.union(s))
s1.update(s)  #the elements of s are added to s1
print(s1,s)

set1={1,2,3,4,5,6}
set2={3,4,5}
print(set1.intersection(set2))
print(set1)
set1.intersection_update(set2)#set1's elements are changed into the intersection of set2 and set1
print(set1)


#symmetric difference=(A Union B)-(A intersection B)
set3={1,2,3,4,5,6}
set4={3,4,5}
print(set3.symmetric_difference(set4))
set3.symmetric_difference_update(set4)# here set3 is changed into the elements remaining after the symmetric difference
print(set3)

#difference and difference_update= A-B
set5={1,2,3,4,5,6}
set6={3,4,5}
print(set6.difference(set5)) #set6-set5
set6.difference_update(set5)
print(set6)


#isdisjoint= two sets are independent of each other that means two sets have no element in common
set7={1,2,3,4,5,6}
set8={3,4,5}
print(set7.isdisjoint(set8))#gives true or false statement

print(set7.issuperset(set8))#checks if the set is superset of another set

set7.add(10)#adds the element to the set
set7.update(set8)#adds the element of the  set into another
#remove and discard
#remove:removes the  element from the set but shows error if the element is not present in the original set
#discard:same as the remove but doesn't show any error if the element is not present
#pop:removes the last item of the set but the catch is that we don't know which item is removed as sets are unordered

del set7 #deletes the entire set
set8.clear()#clears/empties the set

