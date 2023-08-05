# To check prime number or not

n=int(input("Enter N: "))

if n%2!=0:
    for i in range(3, int(n/2)+1, 2):
        if n%i==0:
            print("Is Not Prime")
            break
    else:
        print("Is Prime")
else:
    print("Is Not Prime")
    