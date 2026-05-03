
                #FOR LOOPS
name= "Aditya Talapalle"
for i in name:
    print(i) #matlab every element of name ko print karo
    if i== "a": #for the if statement to be inside the loop,there must be space(Indentation)
        print("pqrs")

colors=["red","green","blue","orange","purple"]
for j in colors:
    print(j)
    for k in j:
        print(k) #nested for loop
c=input("Enter a word: ")
for abc in c:
    print(abc)

#three parameters in range:
#range(stop:int)
#range(start:int,stop:int)
#range(start:int,stop:int,step:int)

for q in range(5): #5 won't be included and starts with 0
    print(q)
print()
for e in range(3,20): # 20 won't be included but 3 will be
    print(e)
print()

for l in range(1,20,2): #jumps by 2 numbers
    print(l)
print()


                        #WHILE LOOPS
z =int(input("To start counting from z to pqr and note that z <= qpr\nEnter z: "))
qpr=int(input("Enter qpr: "))
while z<=qpr: # the loop will continue until the condition you have written(here its z<=qpr) becomes true
    print(z)
    z+=1
t = int(input("Enter a number greater than 40: "))
while t<=40:
    print("incorrect input")
    t = int(input("Enter a number greater than 40: "))


print("you have entered the number:",t)

#while else loop
count = 5
while count>0:
    print(count)
    count-=1
else:
    print("you got out of the while statement and now this is an else statement")

                #BREAK AND CONTINUE
#the break word stops the loop if the condition is met

for ab in range(1,12):
    print("7 x",ab,"=",7*ab)
    if ab==10: #the if statement should be inside the 'for loop'
        break
print()

#the continue word skips the iteration when the condition is met
#writing a code for output 1-12 skipping 10
for cd in range(1,12):
    #the print statement shouldn't be written in this line
    if cd==10: #the if statement should be inside the 'for loop'
      continue
    print("7 x", cd, "=", 7 * cd)


#Emulating the do-while loop
# the do while loop is a function  where the body is executed once irrespective of
#  whether the condition is true or false, then it continues the loop if the condition is true


abc=0
while True:
    print(abc)
    abc+=1
    if abc==1:
        break

print()

#FOR LOOPS WITH ELSE STATEMENTS(video no 35)
for l1 in range(0,5):
    print(l1)
else:  # the statements of the else block are executed after all the iteration of the loop are completed
    print("loop ends after 4")

for l2 in []:
    print(l2)
else:
    print("there was nothing to execute in the loop")

for l3 in range(0,5):
    print(l3)
    if l3==3:
        break
else:
    print("this won't be executed as well")


for l4 in range(0,5):
    print(f"iteration no {l4+1} in for loop")
    if l4==3:
        break
else:
    print("this will be executed after 5")