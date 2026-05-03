#function ke andar usi same function ko agar call kare to use recursion kehte hai

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#Fibonachi series:  F(n)=F(n-1)+F(n-2) and F0=0,F1=1

def fibonachiSeries(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return   fibonachiSeries(n-1)+fibonachiSeries(n-2)

print(fibonachiSeries(6))




