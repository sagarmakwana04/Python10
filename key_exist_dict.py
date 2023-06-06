# Python program to check whether a given key is already exist in a dictionary or not

d={20:'b',30:'c',10:'a'}

def key_exist(x):
    if x in d:
        print("Key exists")
    else:
        print("Key does not exists")
key_exist(20)
key_exist(4)
