# created import module for udf

import udf

while True:
    print('*'*50)
    print('1. Odd Even')
    print('2. Max of Two')
    print('3. Max of Three')
    print('4. Prime')
    print('5. Fibonacci')

    choice=int(input('Enter Your Choice : '))

    if choice==1:
        n=int(input('Enter Value : '))
        udf.odd_even(n)

    elif choice==2:
        a=int(input('Enter Value : '))
        b=int(input('Enter Value : '))
        udf.max_of_two(a,b)

    elif choice==3:
        a=int(input('Enter Value : '))
        b=int(input('Enter Value : '))
        c=int(input('Enter Value : '))
        udf.max_of_three(a,b,c)
    
    elif choice==4:
        n=int(input("Enter Value : "))
        udf.prime(n)

    elif choice==5:
        n=int(input('Enter Value : '))
        udf.fibonacci(n)
    
    else:
        break