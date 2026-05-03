class Temperature:
    def __init__(self):
        self._temp=0
    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,value):
        if value>=-273:
            self._temp=value
        else:
            print("Invalid temperature")

t=Temperature()
t.temp=23
print(t.temp)
q=Temperature()
print(q.temp)

