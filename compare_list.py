# How to compare two list :
"""Python provides multiple ways to compare the two lists. Comparison is the process when the data items of 
are checked against another data item of list, whether they are the same or not."""

# using the set function
lst1 = [11, 12, 13, 14, 15]  
lst2 = [11, 12, 13, 14, 15,] 

a=set(lst1)
b=set(lst2)

if a == b:
    print("List are Same")
else:
    print("List are not same")