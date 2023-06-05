# Python program to find second smallest value from given list

def second_smallest(num):
    if (len(num)<2):
        return
    if ((len(num)==2) and (num[0]==num[1])):
        return
    dup_item=set()
    uniq_item=[]
    for x in num:
        if x not in dup_item:
            uniq_item.append(x)
            dup_item.add(x)
    uniq_item.sort()
    return uniq_item[1]

print(second_smallest([1,2,-5,-8,-2,0]))
print(second_smallest([1,1,0,0,-2,-2,-2]))
print(second_smallest([1,-1,1,0,0,0,2,-2,-2]))
print(second_smallest([2,2]))
print(second_smallest([2]))
print(second_smallest([0]))