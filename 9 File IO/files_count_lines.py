# Python program to count number of lines in a text file


def count_file_lines(fname):
    with open(fname,'r') as f:
        return len(f.readlines())               # return len(f.read()) with give count of no of words in file

print(count_file_lines('test.txt'))
print(count_file_lines('abc.txt'))