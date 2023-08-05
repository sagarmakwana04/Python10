# Sum of three given integers, if two values are equal then sum will be zero

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

sum=a+b+c

if a==b or b==c or a==c:
    print("Sum is : 0")
else:
    print(sum)
