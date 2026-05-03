try:
    a=int(input("Enter the number you want the multiplication table of: "))
    for i in range(1,11):
        print(f"{a}X{i}={a*i}")
except Exception as e:
        print(f"the type of error: {e}")

try:
    a=int(input("Enter the number you want the multiplication table of: "))
    for i in range(1,11):
        print(f"{a}X{i}={a*i}")

except ValueError: #the code will be executed only if the error is ValueError type
    print("wrong datatype input")
except: #if there is no need to find the type of error occurred, we can just use except
    print("there was some type of error")
#IndexError: it's like IndexOutOfBoundException

# FINALLY KEYWORD

# try:
#     #statement which could generate exception
# except:
#     #solution of generated exception
# finally:
#     #block of code which is going to be executed in any situation

l=[1,2,3,4]
try:
    i=int(input("Enter the  Index: "))
    print(l[i])
except:
    print("some error occurred")
finally:
    print("this code will be executed regardless of whether the error occurs or not ")
# finally is used to write the  code in a function to be executed even after you write return statement