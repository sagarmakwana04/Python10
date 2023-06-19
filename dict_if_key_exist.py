# Python program to check whether a given key is already exist in a dictionary or not

d={2:'b',3:'c',1:'a'}

def key_exist(x):           # x will be argument which can be passed during function call
    if x in d:
        print(f'{x} Exist')
    else:
        print(f'{x} Does Not Exist')

key_exist(2)                # as print has been already given in function definition so we just have to function call and pass argument
key_exist(75)