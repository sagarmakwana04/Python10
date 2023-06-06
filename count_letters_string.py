# Python program to create a dictionary from a string. track the count of the letters from a string 

from collections import defaultdict, Counter

str1='Python3 Programming!!!'
dct={}
for letter in str1:
    dct[letter] = dct.get(letter,0)+1
print(dct)