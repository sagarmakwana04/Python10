# Python program to concatenate dictionaries to create new one

d1={1:'A', 2:'B'}
d2={3:'C', 4:'D'}
d3={5:'E', 6:'F'}
d4={}
for i in d1,d2,d3:
    d4.update(i)
print(d4)

