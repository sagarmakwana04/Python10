# program to filter out odd numbers from list using lambda function
li=[1,4,2,3,5,7,11,5,19,13,17,22,97,51,55,50,38,89,27,53]
final_list=list(filter(lambda x: (x%2!=0),li))
print(final_list)
