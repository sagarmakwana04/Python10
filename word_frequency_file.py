# Python program to count frequency of word in text file

from collections import Counter

def word_freq(fname):
    with open(fname,'r')as f:
        return Counter(f.read().split())                # if we use splitlines() will give frequency of lines

# print(word_freq('test.txt'))
print(word_freq('test2.txt'))
print(word_freq('abc.txt'))
