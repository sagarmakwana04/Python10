# Python program to read file line by line and store it to a list
# use with open and readlines method to read line by line and store it into a list


with open('test.txt') as f:
    print(f.readlines())