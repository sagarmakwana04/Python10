# Python program to copy the contents of a file to another file.

# from shutil import copyfile
# copyfile('test2.txt','copy.txt')



# # using for loop
with open('test.txt','r')as f1, open('copy.txt','w')as f2:
    for line in f1:
        f2.write(line)
