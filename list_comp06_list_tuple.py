# creating a list of tuple from two separate list to store name and ages of user
name=["p","q","r"]
age=[17,23,54]
PersonTuple=[(name,age) for name,age in zip(name,age)]
print(PersonTuple)