# Sum of positive given n number of integers
n=int(input("Enter Positive Integer : "))

sum=0

for x in range(1,n+1):
    sum+=x
print(f"Sum of {n} Numbers is : {sum}")


# while loop
n=int(input("Enter N: "))
sum=0
while n>0:
    sum=sum+n
    n=n-1
print("Sum by For Loop:",sum)
