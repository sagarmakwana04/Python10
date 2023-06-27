# if
a=22
b=92
if b>a:
    print("B is greater than A")


# elif
a=77
b=77
if b>a:
    print("B is Greater than A")
elif a==b:
    print("A and B are equal")


# else
a=20
b=100
if b>a:
    print("b is greater than a")
elif b==a:
    print("b is equal to a")
else:
    print("a is greater than b")


# short hand if, used only for one statement
a=100
b=22                    
if a>b: print("a is greater than b")                      

                        
# short hand if else, used when only one statement to execute for both conditions                       
a=int(input())
b=int(input())
print("A is Max") if a>b else print("B is Max")                    
                        

# multiple else on same line                      
a=420                     
b=420                     
print("A") if a>b else print("=") if a==b else print("B")                     
                   

# and keyword is a logical operator 
a=200
b=38
c=800
if a>b and c>a:
    print("Both conditions are true")


# or is a logical operator used to combine conditional statements
a=100
b=66
c=900
if a>b or a>c:
    print("At least one of the condition is True")


# NOT is used to reverse the result
a=33
b=999
if not a>b:
    print("a is NOT grater than b")


# nested if, if inside if, to satisfy two conditions
x=41
if x>10:
    print("Above ten!")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20")


# pass, to store no contend inside if 
a=11
b=899
if b>a:
    pass

i=1
while i<6:
    print(i)
    i+=1