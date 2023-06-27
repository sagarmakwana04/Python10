# Python program to merge two dictionaries 

d1={1:'a',2:'b',3:'c',4:'d'}
d2={'x':100,'y':200,'z':300}

d=d1.copy()
d.update(d2)
print(d)