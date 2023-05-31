# Program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def end_string(s):
    length=len(s)
    if length>2:
        if s[-3:]=='ing':
            s+='ly'
        else:
            s+='ing'
    return s

print(end_string('pq'))
print(end_string('xyz'))
print(end_string('typing'))
print(end_string('hack'))
print(end_string('program'))