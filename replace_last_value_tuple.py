# Python program to replace last 2 value of tuples in a list

l=[(10,20,40),(40,50,70),(70,80,90)]
print([t[:-2] + (99,100,) for t in l])