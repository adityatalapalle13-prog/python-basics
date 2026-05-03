import time
timestamp=time.strftime('%H:%M:%S')

print(timestamp)
if timestamp>= "12:00:00" and timestamp< "18:00:00":
    print("good afternoon sir")
elif timestamp>="18:00:00":
    print("Good evening sir")
else:
    print("good morning sir")


#Kaun banega crorepati,
questions=[["What is the capital city1 of India","Dehli","Mumbai","Banglore","Kolkata"], #comma makes them different lists into elements
           ["What is the capital city2 of India","Dehli","Mumbai","Banglore","Kolkata"],
           ["What is the capital city3 of India","Dehli","Mumbai","Banglore","Kolkata"],
           ["What is the capital city4 of India","Dehli","Mumbai","Banglore","Kolkata"],
           ["What is the capital city5 of India","Dehli","Mumbai","Banglore","Kolkata"]]
levels=[100,200,300,400,500,600]

#EXERCISE 4
 #If the word contains at least 3 characters, remove the first letter and append it at the end
 #now append three random characters at the starting and the end
 #else:
     #simply reverse the string

#Decoding:
#if the word contains less than 3 characters reverse it
# else:
  #    remove 3 random characters from start and end now remove the last letter and






