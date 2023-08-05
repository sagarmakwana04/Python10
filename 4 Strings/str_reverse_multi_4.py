# Python program to print reverse string if length of string is multiple of four

def reverse_str(s):
    if len(s)%4==0:
        return s[::-1]
    else:
        return s

print(reverse_str('help'))
print(reverse_str('help me'))