x=5 #this is also a global variable(which is not inside any function)
def myfunction():
    global x
    x=4# the global keyword makes this value true for even outside the function
    y=3
    print(x,y)
myfunction()
print(x)

def anotherfunction():
    global x
    x=6
anotherfunction()# even if you assign a global variable in a function, you need to call the function at least once for them
print(x)#to change the value