# Python program to read the file line by line and to store it into a variable


with open('test.txt') as myfile:
    data=myfile.readlines()             # here, we made variable and then read that file
    print(data)

with open('test2.txt') as myfile:
    data=myfile.readlines()
    print(data)
    