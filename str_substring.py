# program to find occurrance of a substring in a string

string="dadadadadadada"

count=sum(1 for i in range(len(string)) if string.startswith("dada",i))
print(count)