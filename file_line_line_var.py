# Python program to read the file line by line and to store it into a variable


with open('test.txt') as myfile:
    data=myfile.readlines()             # we made variable and then read that file
    print(data)