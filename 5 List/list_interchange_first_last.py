# Python program to intechange first and last elements from given list
# by making temp varialble and swaping the value

l=[1,2,3,4,5]
temp=l[0]
l[0]=l[-1]
l[-1]=temp

# l[0],l[-1]=l[-1],l[0]       # it can also be solved using this method

print(l)
