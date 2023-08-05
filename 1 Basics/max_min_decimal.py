# Python program to find the maximum and minimum numbers from the specified decimal numbers

from decimal import *
data=list(map(Decimal, '2.52 3.75 7.01 5.83 6.58 0.003 1.111'.split()))

print("Maximum : ",max(data))
print("Minimum : ",min(data))