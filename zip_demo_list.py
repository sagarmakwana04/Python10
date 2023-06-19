# Why we use zip function in python :
# In Python, the zip() function is used to combine two or more lists (or any other iterables) into a single iterable, 
# where elements from corresponding positions are paired together. The resulting iterable contains tuples, 
# where the first element from each list is paired together, the second element from each list is paired together, and so on.

name=['Sagar','Meet','Kuldip','Jay','Prince']
rno=[4,2,13,3.2,7]


print(set(zip(name,rno)))