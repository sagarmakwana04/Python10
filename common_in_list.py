# Python function that takes two lists and returns true if they have at least one common member

def commonData (l1,l2):
    result = False
    for x in l1:
        for y in l2:
            if x==y:
                result = True
                return result

print(commonData([1,2,3,4,5],[5,6,7,8,9]))
print(commonData([1,2,3,4,5],[6,7,8,9]))
