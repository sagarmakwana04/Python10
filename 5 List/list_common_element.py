# Python function that takes two lists and returns true if they have at least one common element

def common_data(l1,l2):
    res=False
    for x in l1:
        for y in l2:
            if x==y:
                res=True
                return res

print(common_data([1,2,3],[3,4,5]))
print(common_data([2,1],[6]))
print(common_data([1],[True]))
