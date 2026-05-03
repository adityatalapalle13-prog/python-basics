# 2 types of functions:
# built-in functions: doesn't need def keyword
# user defined functions: needs def keyword



# Syntax:
#
# # def NameOfTheFunction(Parameters):
# #     body
# #     return


def calculategmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)

calculategmean(3,5)

def islesser():
    pass   #this means Kuch karne ki zarurat nhi hai
            #if function doesn't contain a body, pass word is used to avoid errors

#FUNCTION ARGUMENTS
# There are 4 types of arguments in a function:
# default
# keyword
# variable length
# Required

                #Default arguments
def average(a=2,b=3): # you can create a function with defined parameters, which will be set as default and
    print("the average is ",(a+b)/2) #you can change them while calling the function

average()
average(6,8)
average(5)#it will take a as 5, while  be will remain 3
average(b=8) # here a will remain 2


                #keyword
average(6,5)
average(b=5,a=6) #the order in which the arguments are written does not matter
                 # because interpreter takes the value according to the keyword

                 #Required
#if we don't  set a default to the variables while defining the function then
#it is required to give a value to it whenever we call the function

def average2(c,d=5): # since we haven't set any value for c here we need to assign a value whenever we call this function
                     #seems we cannot write non defined parameters after the defined ones in bracket
    print("the average is ",(c+d)/2)

average2(5)

                    #Variable length

def average3(*numbers): # *numbers means it became iterable(takes in as tupple)
    sum=0
    for i in numbers:
        sum=+i

    print("the average is ", sum/len(numbers)) #this doesn't come under loop but in function

average3(6,5,4,8,6,45,7)

def name(**name): #this is a dictionary(will be learnt in future)
    print(type(name))#to check the type of the name
    return "Hello "+name["fname"]+name["mname"]+name["lname"]

person1=name(fname="Aditya ",mname="Satyanarayana ",lname="Talapalle")
print(person1)