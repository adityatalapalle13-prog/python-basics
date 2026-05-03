#OOPs
#CLASSES
class Person:
    name=""  # you need to define if these objects are strings or integers
    age=0
    occupation=""


    def info(self): #self word is needs to be written to use the values assigned of that particular objects when calling this function
                    #self word is used in almost all the functions inside a class
        print(f"{self.name} of age {self.age} is a {self.occupation}")



student1= Person()
student1.name="abcd"
student1.age=18
student1.occupation="student"
student1.info()

#CONSTRUCTORS
#def __init__(self):
#   code

#two types of constructors:
#paramterized : accepts parameters along with self
#default: accepts only self(mostly used to initialize an object and write print statement)


class Student:

    def __init__(self, rollnum, classnum):
        self.rollnum= rollnum
        self.classnum=classnum
        print(f"A new student has joined of rollnumber {rollnum} and class number {classnum}")


aditya=Student("rvce25bai044","cia")

