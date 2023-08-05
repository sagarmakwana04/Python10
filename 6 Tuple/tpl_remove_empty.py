# Python program to remove empty tuples from a list of tuples

tuples=[(),(5,4),(1,2,3),(),(3,2,1),()]

def Remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
print(Remove(tuples))


# # or
# tuples.remove(())
# print(tuples)

