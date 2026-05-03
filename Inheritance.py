class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def intro(self):
        print(f"the name and the id of the employee are {self.name},{self.id}")


class Programmer(Employee):
    def greet(self):
        print(f"hello I'm a programmer, I'm {self.name} and my id is {self.id}")

e1=Employee("Aditya",13)

e1.intro()
e2=Programmer("abcd",15)
e2.intro()
e2.greet()





