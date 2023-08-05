# Lambda function examples

# to find cube of any number using lambda function
n=int(input("Enter Value:"))
lambda_cube=lambda y: y**3
print(lambda_cube(n))       # lambda function can take only one expression


# example of lambda function using if else to find max number from two integers
max=lambda a,b: f"{a} is Max" if a>b else f"{b} is Max"
print(max(948,983))


# program to filter out odd numbers from list using lambda function
li=[1,4,2,3,5,7,11,5,19,13,17,22,97,51,55,50,38,89,27,53]
final_list=list(filter(lambda x: (x%2!=0),li))
print(final_list)


# to transform all elements of a list to upper case using lambda and map function
company=['dell','hp','logitech','tops','asus','google','accenture','oracle']
uppered_company=list(map(lambda company: company.upper(),company))
print(uppered_company)
title_company=list(map(lambda company: company.title(),company))
print(title_company)


# program to find reciprocal of given number using lambda function
num=int(input('Enter Value:'))
reciprocal=lambda num: 1/num
print(reciprocal(num))