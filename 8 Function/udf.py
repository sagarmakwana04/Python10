# make udf programs
# make another file import udf
# while true: print choices of function, get choice from user
# if choice==1 function that def, elif 2,3,.. else:break


def odd_even(n):
    if n%2==0:
        print(f'{n} is Even Number')
    else:
        print(f'{n} is Odd Number')

def max_of_two(a,b):
    if a>b:
        print(f'{a} is Max')
    else:
        print(f'{b} is Max')

def max_of_three(a,b,c):
    if a>b:
        if a>c:
            print(f'{a} is Max')
        else:
            print(f'{c} is Max')
    elif b>c:
        print(f'{b} is Max')
    else:
        print(f'{c} is Max')

def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(f'{n} is Not Prime')
                break
        else:
            print(f'{n} is Prime')
    else:
        print(f'{n} is Not Prime')

def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=' ')
        a,b=b, a+b
        
    print()             # to get last choice printed into new line