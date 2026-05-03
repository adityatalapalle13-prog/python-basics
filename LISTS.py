#lists are ordered collection of data items
# they store multiple items in a single  variable
# list items are separated by commas and enclosed within square  brackets
#lists are changeable unlike tuples

marks=[1,   2 ,  3 , "Adi" ,True] #adi itself is an element as a whole
#     [0]  [1]  [2]   [3]   [4]
#     [-5] [-4] [-3]  [-2]  [-1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

#List index --> starts with 0, same as string index but here 1 element gets the index number as a whole instead of each char

#To check if an element is present in a list
if "Adi" in marks:
    print("yes")
else :
    print("no")

#same thing applies for string as well
if "Adi" in "Aditya":
    print("yes")
else:
    print("no")

print(marks[1:4]) # 4 won't be included, same as string
print(marks[1:5:2])# start:end:jump/step
print(marks[::2])

#List comprehension
list0=[i for i in range(1,11)]
print(list0)

list2=[i for i in range(1,11) if i%2==0]
print(list2)

                #LIST METHODS
l=[1,2,3,4,5,6]
print(l)
l.append(7) #used to add element to the list as a last element
print(l)

l2=[35,45,1,1,2,3,4,5]
l2.sort() # sorts the list in ascending order, number in ascending order and words in order of A-Z(like in dictionary)
print(l2)
l2.sort(reverse=True)

print(l2)

print(l2.index(45))#gives the index number of the element
                   #gives the index number of the first occurrence of the element even if there are multiple

print(l2.count(1))#counts the number of times the element is repeated in the list

m=l
m[0] =0 #since we have assigned m=l if we were to change m, l will also be changed
print(l)
m=l.copy() #that won't happen here, m and l here are independent
l.insert(1,57)#(index num,element that you wanna add), the previous element of that index num won't be replaced,the previous one will shift to the next index number

m1=[67,69,71]
l.extend(m1) #it means add the elements of m1 to l

k=l+m+m1 #we can concatenate lists


