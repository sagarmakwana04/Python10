# Python program to print a dinctionary where keys are numbers between 1 and 15

n=int(input('Enter N : '))

d=dict()                    # we taken blank dict

for i in range(1,n+1):       
    d[i]=i                  # d[i]=i , store iteration of i inside d, eg,. d[1]=1, d[2]=2, here d[1] is key and =1 is value
                            # d[i]=i**2 will print sqrt of n numbers
print(d)