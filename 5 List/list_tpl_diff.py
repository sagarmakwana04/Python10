# What is Tuple? 
"""A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences 
between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, 
whereas lists use square brackets.
"""


# difference between list and tuples
"""
List:
> List are mutable
> Implication of iteration is time-consuming
> Better for performing operations, such as insertion and deletion
> Lists consumes more memory
> Lists have several built-in methods
> Unexpected changes and errors are more likely to occur


Tuple:
> Tuple are immutable(not changable)
> Implication of iteration is comparatively faster
> Tuple data is appropriate for accessing for elements
> Consumes lesser memory as compared to the list
> Tuples does not have many built-in methods
> In a tuple, it is hard to take place
"""


# example to show mutability of list
l=[1,2,3,4,4,5,7,8,9]
l[4]=77
print(l)


# example of tuple can not be modified
t=(1,2,3,4,5,6,7)
t[3]=77
print(t)