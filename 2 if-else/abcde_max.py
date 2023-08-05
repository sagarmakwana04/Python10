# Max of ABCDE

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))
e = int(input("Enter e : "))

if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("A is Max")
            else:
                print("E is Max")
elif b>c:
    if b>d:
        if b>e:
            print("B is Max")
        else:
            print("E is Max")
elif c>d:
    if c>e:
        print("C is Max")
    else:
        print("E is Max")
elif d>e:
    print("D is Max")
else:
    print("E is Max")
