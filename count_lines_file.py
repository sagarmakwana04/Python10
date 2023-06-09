# Python program to count number of lines in a text file


def count_file_lines(fname):
    with open(fname,'r') as f:
        return len(f.readlines())

print(count_file_lines('test.txt'))
print(count_file_lines('abc.txt'))
print(count_file_lines('D:\Python\9 File IO\myfile.txt'))