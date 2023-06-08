# Python program to read file line by line and store it to a list
# to read file line by line and to print it into a list, we use with open method and readlines() function, with open will automatically close the file 


# Method 1 using for loop and to read line by line and store in list of individual lines
f=open('test.txt','r')
for i in f:
    print([i])
f.close()



# using with open() method and print line by line and store into a list
with open('test.txt') as f:
    print(f.readlines())


# read another file
with open('test2.txt') as f:
    print(f.readlines())
