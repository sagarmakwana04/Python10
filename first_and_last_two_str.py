# Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

def both_str_ends(s):
    if len(s)<2:
        return ''
    else:
        return s[:2]+s[-2:]

text=input("Enter String : ")
print(both_str_ends(text))