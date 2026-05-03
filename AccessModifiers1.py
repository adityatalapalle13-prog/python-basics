class Employee:
    def information(self):
        self.__salary=0
        return self.__salary

a=Employee()
a.information()#here, the function needs to be called at least once for salary variable to be created
print(a._Employee__salary)


class Employee1:
    def __init__(self):
        self.__salary2=0


b=Employee1()
print(b._Employee1__salary2)
