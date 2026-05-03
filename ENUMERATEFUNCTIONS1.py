marks=[12,55,54,98,65,32,41]
index=0
for abc in marks:
    print(abc)
    if index==3:
        print("this will be printed after the 4th element")
    index+=1

print()
for index, abcd in enumerate(marks):
    print(index,abcd)
    if(index==3):
        print("this will be printed after the 4th element\n and there is no need for index+=1")

print()
for ind, abcde in enumerate(marks,start=1):
    print(ind,abcde)
    if(ind==3):
        print("this will be printed after the 3rd element\n and there is no need for index+=1")
