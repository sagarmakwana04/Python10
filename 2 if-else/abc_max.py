
# proram to check max from abc

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

if a>b:
    if a>c:
        print("A is Max")
    else:
        print("C is Max")
elif b>c:
    print("B is Max")
else:
    print("C is Max")
