# if statement fundamental concept
i=10
if i>15:
    print("10 is less than 15")
print("I am not in if")


# if else
i=20
if i<15:
    print("i am smaller than 20")
    print("i am inside if block")
else:
    print("i am greater than 20")
    print("i am inside else block")
print("i'm not in if and not in else block")


# if else if else chain
letter="A"
if letter =="B":
    print("Letter is B")
else:
    if letter =="C":
        print("Letter is C")
    else:
        if letter=="A":
            print("Letter is A")
        else:
            print("Letter is'nt A, B or C")