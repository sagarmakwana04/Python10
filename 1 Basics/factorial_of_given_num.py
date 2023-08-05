# This is Programme to find factorial of given number 

num = int(input("Enter n: "))

factorial = 1
for i in range(1, num+1):
    factorial=factorial*i
print("Factorial of", num, "is:", factorial)


# Method 2
import math
print(math.factorial(5))