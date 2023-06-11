# Python program to find frequency on characters in a given string

# Python program to find character frequency

# using collection.Counter()
from collections import Counter
string="Python,Programming,java,html,css,django,mysql,oops,javascript,tkinter"

freq=Counter(string)

print(str(freq))        # this will give in higher to lower order of frequencies 


# using loop
frequency={}

for i in string:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
        
print(str(frequency))