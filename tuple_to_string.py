# Python program to convert a tuple to a string

t=('P','y','t','h','o','n','-','3')
print(t)

# using function
def convertTuple(t):
    str=''
    for i in t:
        str=str+i
    return str
str=convertTuple(t)
print(str)


# using for loop
for i in t:
    print(i, end="")