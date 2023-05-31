# Python program to print reverse string if length of string is multiple of four

def reverse_string(s):
    if len(s)%4==0:
        return s[::-1]
    else:
        return s
    
text=input("Enter String : ")
print(reverse_string(text))