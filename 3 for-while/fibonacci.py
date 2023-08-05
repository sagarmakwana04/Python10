# 0 1 1 2 3 5 8 13 21 34 55 89 144

n=int(input("Enter Value : "))

a,b=0,1

while b<n:
    print(b,end=" ")
    a,b=b, a+b
