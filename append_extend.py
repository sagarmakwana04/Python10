# append() : It adds an element at the end of the list. The argument passed in the append function is added as a 
# single element at end of the list and the length of the list is increased by 1.
lst=["Tit","for"]
lst.append("Tat")
print(lst)


# extend() : This method appends each element of the iterable (tuple, string, or list) to the end of the list 
# and increases the length of the list by the number of elements of the iterable passed as an argument
lst2=["hello","welcome",]
lst2.extend(["python","programming","with","django"])
print(lst2)