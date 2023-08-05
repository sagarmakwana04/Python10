# Python program that user to enter only odd number, else will raise an exception

try:
    n=int(input("Enter N :"))
    assert n%2!=0
except:
    print("Not an odd number!")