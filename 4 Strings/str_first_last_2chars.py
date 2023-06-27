# Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

def first_last_two(s):
    if len(s)>2:
        return s[:2] + s[-2:]
    else:
        return " "
    
print(first_last_two('python'))
print(first_last_two('da'))
print(first_last_two('Django'))
print(first_last_two('motorola'))
print(first_last_two('string'))