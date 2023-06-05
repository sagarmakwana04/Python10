# Python program to unzip a list of tuples into individual lists

tpl=[(10,20,40,80),(40,50,70,90)]
print(list(zip(*tpl)))