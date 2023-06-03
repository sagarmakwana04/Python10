# program to remove duplicates from list

# method 1 using set function
duplicates=[2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicates)))


# method 2 using logical function
def Remove(duplicate):
    final_list=[]
    for num in duplicates:
        if num not in final_list:
            final_list.append(num)
    return final_list
print(Remove(duplicates))
