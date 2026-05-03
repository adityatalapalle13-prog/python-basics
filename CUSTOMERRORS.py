#we raise error to serve our purpose
a=int(input("enter a number between 5 and 9: "))
if a<5 or a>9:
    raise ValueError("The integer should be between 5 and 9: ")

#defining custom exceptions:
# class CustomError(Exception):     (Syntax)
#     code
#     pass
# try:
#     code
# except CustomError:
#     code

