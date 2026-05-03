# old method
letter="Hey my name is {} and I'm from {}"
country="India"
name="Aditya"
print(letter.format(name,country))

letter="Hey my name is {1} and I'm from {0}"#the 0 and 1 indicates the order of taking input regardless of in which order you fill in
country1="India"
name2="ABCD"
print(letter.format(country1,name2))

#fstring method
print(f"Hey my name is {name} and I'm from {country}")
price=100.59999999999
rate=f"for only {price:.2f} rupees"
print(rate)
print(f"{30*85}")#the answer will be still a string
print(f"{{double curly brackets are used to retain one bracket in output}}")

#DOCSTRINGS
def square(n):
    ''' Takes in a number n, returns the  square of n'''
    print(n**2)
square(5)
print(square.__doc__)

def square1(a):
    print(a) #if the doc string line is not just after the def line, then it wouldn't work
    ''' Takes in a number n, returns the  square of n'''
    print(a**2)
square1(5)
print(square1.__doc__)

#PEP8
#python enhancement proposal




