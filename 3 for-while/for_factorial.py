# Python program to find factorial of given number

num=int(input("Enter Number : "))
fac=1
for x in range(1,num+1):
    fac=fac*x
print(fac)


# using built in function
import math
def factorial(n):
    return math.factorial(n)
n=int(input("Enter N : "))
print(factorial(n))
