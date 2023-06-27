# Python program to count number of characters in text file


# # to varify count: 
# f=open('test.txt')
# for i in f:
#     print(len(i))
# print(73+96+109+38+32+49+88+118+87+79)



def count_char(fname):
    with open(fname,'r') as f:
        return len(f.read())

print(count_char('test.txt'))
print(count_char('abc.txt'))
print(count_char('test2.txt'))
print(count_char('D:\Python\9 File IO\myfile.txt'))