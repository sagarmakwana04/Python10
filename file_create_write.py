# What is file function ?
'''A file is a container in computer storage devices used for storing data.
When we want to read from or write to a file, we need to open it first. When we are done, 
it needs to be closed so that the resources that are tied with the file are freesed.
Hence, in Python, a file operation takes place in the following order:

Open a file
Read or write (perform operation)
Close the file'''


# What is keyword to create and write in files
'''There are two things we need to remember while writing to a file.

If we try to open a file that doesn't exist, a new file is created.
If a file already exists, its content is erased, and new content is added to the file.
In order to write into a file in Python, we need to open it in write mode by passing "w" inside open() as a second argument.'''


with open('test2.txt', 'w') as file2:
    file2.write('Programming is Fun.\n')
    file2.write('Python Programming for beginners')


# read that file
with open('test2.txt','r')as f:
    print(f.read())