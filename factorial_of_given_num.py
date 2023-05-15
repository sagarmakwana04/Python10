# Programme to find factorial of given number 

num = int(input("Enter num : "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print("Factorial of", num, "is :", factorial)

