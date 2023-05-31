# Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def not_and_poor(s):
    snot = s.find('not')
    spoor =s.find('poor')

    if spoor>snot and snot>0 and spoor>0:
        s=s.replace(s[snot:(spoor+4)], 'good')
        return s
    else:
        return s

print(not_and_poor('The lyrics is not that poor!'))
print(not_and_poor('The lyrics is poor!'))