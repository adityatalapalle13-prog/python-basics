dict1={
    "Name":"Aditya",
    "Greet":"Hello",
    656:"Aditya's ID"}
print(dict1)
print(dict1[656])# gives the value of the key you input
print(dict1.get(123))#this doesn't give error if the element doesn't exist
#dictionaries are ordered pairs, separated by commas inside the curly brackets
print(dict1.keys())#keys means the left part
print(dict1.values())#values means the right part
print()

for abc in dict1.keys():
    print(abc,":",dict1[abc])

# DICTIONARY METHODS
Info ={1:98,2:95,3:89}
Info2={4:79,5:99}
Info.update(Info2)#adds the element of Info2 to Info
print(Info)
Info.pop(1)
print(Info)
Info.popitem()#removes the last element of the dictionary
print(Info)
del Info[4] #deletes the element
print(Info)
Info.clear()#the elements of the dictionary are removed but the empty dictionary still exists
print(Info)

del Info #deletes the dictionary
















