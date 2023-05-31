# program to find occurrance of a substring in a string

str="dadadadadadada"
sub_str="dada"

count=sum(1 for i in range(len(str)) if str.startswith('dada',i))
print("Occurrence of substring is :", count)