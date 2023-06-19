# Python program to write a list to a file.

color=['Green','Red','Blue','White','Black','Orange','Yellow']

with open('test3.txt','w')as f:
    for i in color:
        f.write('%s \n' %i)