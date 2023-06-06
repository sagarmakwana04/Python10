# Python function to check whether a number is perfect or not
# perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3

def perfect_number(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum==n
    
print(perfect_number(6))
print(perfect_number(28))
print(perfect_number(85))
print(perfect_number(1))