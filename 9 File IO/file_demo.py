# # How to read files in python
# f=open('demofile.txt','r')
# print(f.read())


# # # if file is located in different location then have to specify the path
# # f=open('D:\Python\Python Programs\welcome.txt','r')
# # print(f.read())


# # Read only part of the file
# f=open('demofile.txt','r')
# print(f.read(17))               # if 17 is given as argument then it will upto/all 17 character


# # Read lines
# f=open('demofile.txt','r')
# print(f.readline())
# print(f.readline())


# # By looping through the lines of the file, you can read the whole file line by line
# f=open('demofile.txt','r')
# for i in f:
#     print(i)


# # Close file : it is always good practice close the file when you are done with it
# The close() command terminates all the resources in use and frees the system of this particular program.
# f=open('demofile.txt','r')
# f.close()



# # Write to an existing file
# # you must add a parameter to the open() function
# # "a" - Append - will append to the end of the file
# # "W" - Write - will overwrite any existing content


# # Creat, Write file
# f=open('writedemo.txt','w')
# f.write('Now the file has some content!')
# f.close()


# # Open,Read that created file
# f=open('writedemo.txt','r')
# print(f.read())


# # Open the file and overwrite the content
# f=open('writedemo2.txt','w')
# f.write('Woops! you have overwritten the file content!')

# f=open('writedemo2.txt','r')
# print(f.read())
# f.close()


# # Create a new file
# # 'x' - Create - will create a new file, returns an error if already exist
# # 'a' - Append - will create a new file, if the specified file does not exist
# # 'w' - Write - will create a new file, if the specified file does not exist

# # f=open('myfile.txt','x')        # a new empty file is created

# f=open('myfile2.txt','w')


# # Append File : this will add text in the last of file
# f=open('demofile.txt','a')
# f.write("Jsca, World!\n")

# f=open('myfile.txt')        # see append text
# print(f.read())


# with open ('myfile.txt','a') as f:          # this will automatically close the file
#     f.write('Hey i am inside with\n')



# # file remove/exist/folder delete
# import os

# # Remove file
# os.remove('myfile2.txt')


# # Check if file exist : 
# print(os.path.exists('writedemo.txt'))
# print(os.path.exists('writedemo2.txt'))


# # Delete folder 
# os.rmdir('demofolder')


# # rename file
# os.rename('writedemo.txt','write.txt')
