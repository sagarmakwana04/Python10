# Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends 
# with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

def add_ing_ly(str1):
    length=len(str1)                # created variable store length of str1
    if length>2:                    # str1 will go inside if block only if length>2, instead no change
        if str1[-3:]=='ing':        # if str1 ends(last 3 letter) with 'ing' then add 'ly' after ing at its last, eg., string --> stringly
            str1+='ly'              
        else:   
            str1+='ing'             # else add 'ing' if there is not 'ing' at last eg., abc --> abcing
    return str1

print(add_ing_ly('ab'))
print(add_ing_ly('abc'))
print(add_ing_ly('read'))
print(add_ing_ly('string'))
print(add_ing_ly('walking'))
