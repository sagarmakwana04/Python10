# Python program to write a list to a file.

color=['Greeen','Red','Blue','White','Black','Orange','Yellow']

with open('test3.txt','w')as f:
    for i in color:
        f.write('%s \n' %i)

with open('test3.txt','r')as f:
    print(f.read())
