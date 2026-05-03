#Conditional operators
# <, >, <=, >=, ==, !=

a= int(input("enter ur age: "))

if(a>=18):
    print("you can drive") #the pass word seems to be usable here too(from Functions)
    #the space is necessary for if function to work, the space signifies that the code is for if-else
    #if there is no space then it means that you have come out of the if-else function
else:
    print("you cannot drive")
print("this doesn't come under if-else statement")

num=int(input("enter a number: "))
if(num<0):
    print("number is negative ")
elif(num==0):
    print("number is zero")
else:
    print("number is positive")
#first it checks the condition of if, if its true, then it executes the code under if statement
#then it goes from top to bottom, and executes the code whenever it meets the condition,and ignores everything after that

#NESTED IF ELSE STATEMENTS:
nu2=int(input("enter a number: "))
if nu2<0:
    print("number is negative ")

elif nu2>0 :
    if nu2>=10:
        print("number is greater than or equal to 10")
    else:
        print("number is between 1 and 9")

else:
    print("number is zero")
    #if,elif and else align under same vertical line

#MATCH CASE STATEMENTS:(similar to switch case statements of java)
#here there's no need to use break word
x= int(input("enter a number: "))
match x:
    case 10:
        print("you have entered 10")
    case _:      # underscore is used to denote default case
        print("you have entered a number other than 10 ",x)


#mixing if and match statements
y= int(input("enter your age: "))
match y:
    case 18:
        print("congrats on becoming an adult")
    case _ if y>18:
            print("you are already an adult ",y)
    case _ if y<18:
        print("you are still a child")


#shorthand if else statements (lect 41)
a=30
b=545
print("A is of higher value") if a>b else print("=") if a==b else print("B is of higher value")
print("abcd") if a>b else ""
c=9 if a>b else c=0 #use shorthand if else statements only when needed to write simple statements
                    #for code containing multiple lines it's better to write normal if else statements
