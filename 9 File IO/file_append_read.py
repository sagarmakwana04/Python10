# Python program to append file and display file text

# append file
with open('abc.txt','a')as f:
    f.write('\nappending in python file handling')


# read file
with open('abc.txt','r')as f:
    print(f.read())