# Python program to read first n lines of file


n = int(input("Enter Lines To Read : "))
f = open("test3.txt","r")

for i in range(n):
	print(f.readline())
f.close()