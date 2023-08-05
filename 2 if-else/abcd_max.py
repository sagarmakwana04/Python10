# ABCD which number is maximun

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))

if a>b:
    if a>c:
        if a>d:
            print("A is max")
        else:
            print("D is max")
elif b>c:
    if b>d:
        print("B is max")
    else:
        print("D is max")
elif c>d:
    print("C is max")
else:
    print("D is max")