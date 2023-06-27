# Python program to convert a tuple to a string

# Method 1
t1=('P','y','t','h','o','n','-','3')
for i in t1:
    print(i,end='')



# Method 2
print()
def convertTuple(t1):
    str=''.join(t1)
    return str

print(convertTuple(('hello',' ','world')))
print(convertTuple(('v','s',' ','code')))