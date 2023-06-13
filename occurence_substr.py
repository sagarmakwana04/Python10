# To count occurence of a substring in a given string

s="dadadadadadadada"

count=sum(1 for i in range(len(s))  if s.startswith('dad',i))
print(f"Occurence of 'dad' in {s} is {count} times")