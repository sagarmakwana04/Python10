# program to find grade of student distinction, first class, sencond, pass or failed using percentage

rno=int(input("Enter Roll Number: "))
sname=(input("Enter Name of Student: "))
s1=int(input("Enter Marks of Subject 1: "))
s2=int(input("Enter Marks of Subject 2: "))
s3=int(input("Enter Marks of Subject 3: "))

total=s1+s2+s3
per=total/3

print("Result")
print("Roll Number:",rno)
print("Student Name:",sname)
print("Total Marks:",total)
print("Percentage:",per)

if per>=70:
    print("Grade: Distinction")
elif per>=60:
    print("Grade: First Class")
elif per>=50:
    print("Grade: Second Class")
elif per>=40:
    print("Grade: Pass Class")
else:
    print("Failed")


# # to give grade of student based on given percentage
# per=int(input("Enter Your Percentage : "))

# if per<=100 and per>=80:
#     print("Congratulations! A Grade")
# elif per<=80 and per>=60:
#     print("B Grade")
# elif per<=60 and per>=35:
#     print("C Grade")
# elif per<35:
#     print("Filed")
# else:
#     print("Invalid Input!")