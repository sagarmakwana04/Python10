# Python program to check multiple keys exist in a dictionary

d={1:'a',2:'b',3:'c',4:'d'}

def MulKeyExist(x):
    if x in d:
        print("Key exist")
    else:
        print("key does not exist")

MulKeyExist(1)
MulKeyExist(2)
MulKeyExist(4)
MulKeyExist(8)