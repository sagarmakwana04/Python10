# Python function to check whether a number is perfect or not
# perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3


def perfect_num(n):
    sum=0
    for x in range(1,n):
        if n%x==0:          # n ne x vade divide karta jo module 0 aave to e j sum ma add thai
            sum=sum+x
    return sum==n

print(perfect_num(6))
print(perfect_num(28))
print(perfect_num(9))
print(perfect_num(67))