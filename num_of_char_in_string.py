# to find frequency of character in string

count_str="Python Programming!!!"

frequency={}

for i in count_str:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(f"Count of all characters in {count_str} is :\n" + str(frequency))