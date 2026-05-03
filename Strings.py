sentence="He said, \"He wants to eat an apple\""
print(sentence)
sentence2= 'He said,"he wants to eat an apple"'
print(sentence2)
''' hello''' # this seems to be for comments(this is called docstrings and will be learnt in future)
             # also for multi lined string
sentence3=""" hello my name is aditya        
I'm currently studying in a shithole college
and using triple single quote or double quote allows you
to write in multiple lines of code"""
print(sentence3)

#keywords in strings
print(sentence2[0])# prints the char at given index, index starts with 0

for abcd in  sentence:
    print(abcd)  # will learn about them in loops

#String slicing and operations
print(len(sentence3)) # len(string name) gives the length

name="aditya Talapalle"
print(name[0:6]) #prints the chars of name from index number 0 to 5(not 6), last  number will be always excluded
print(name[:6]) # by default, it will take as 0
print(name[:]) #this will print until the last character
print(name[:len(name)-3])
print(name[:-3])# line 26 and 27 are same
print(name[-7:-1])# here, -1 equals e, and it won't be included in the output but -7 will be included

print(name.upper()) #converts all the letters to upper case

print(name.lower())

print(name.rstrip("lle"))# it removes the part of the string you input, you can only remove the ending part of the string

print(name.replace("aditya","ABCD")) #you cannot ignore the  case here, uppercase letters should be written in uppercase

print(name.split(" "))

print(name.capitalize()) #This converts the first letter to uppercase and converts all other letters into lowercase

print(name.center(50)) # 50=parameter

print(name.count("a")) # counts the no of time the string occurred in the variable

print(name.endswith("lle")) #gives true of false

print(name.endswith("ya",0,6)) #checks if it ends with ya if you slice the string with given index numbers

print(name.find("T")) #gives the index number of the string you have input, give -1 if it couldn't find the string we have input
                      #also only gives the first occurrence

print(name.index("T")) #same as find but gives error if not found

print(name.isalnum()) # check if the string contains only a-z,A-Z and 0-9, false if it contains any other punctuations(even space)

print(name.isalpha()) # true if it only consists of a-z,A-Z

print(name.islower()) #true if all the letters are lowercase

print(name.isprintable())

name1="    "
print(name1.isspace()) #true if string contains only space
print(name.isspace())

print(name.istitle()) #true if every word of the string is capitalized

print(name.isupper())

print(name.startswith("adi"))

print(name.swapcase()) #swaps the cases of all the  letter in the string

print(name.title()) # capitalizes every first letter of all the words inside the string

