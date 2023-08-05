# Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# 1.find() 2.if spoor>snot 00 3.replace 


# 1
def replace_not_poor(s):
    snot = s.find('not')
    spoor =s.find('poor')

    if spoor>snot and snot>0 and spoor>0:               # first check that not follows poor(spoor>snot) then snot>0 and spoor>0 to check that both are after zero
        s=s.replace(s[snot:(spoor+4)], 'good')          # used replace() meaning of (:) is bw snot:spoor, +4 means replace 4 letter or poor by good
        return s
    else:
        return s

print(replace_not_poor('The lyrics is not that poor!'))
print(replace_not_poor('The lyrics is poor!'))
print(replace_not_poor('the give data are not that much poor than previous'))


# 2
def replace_python_program(s):
    spython=s.find('python')
    sprogram=s.find('program')

    if sprogram>spython and spython>0 and sprogram>0:
        s=s.replace(s[spython:(sprogram+7)],'code')
        return s
    else:
        return s
print(replace_python_program('Write a python program'))
print(replace_python_program('Write a python ver 3 program to insert a string in the middle of a string'))
print(replace_python_program('Write a python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.'))