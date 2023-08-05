# Python program to replace last 2 value of tuples in a list

l=[(10,20,40,30,50)]

print([t[:-1] + (99,) for t in l])         
# print([t[:-1]+(99,88,77) for t in l])         # this will add items at last

