# Python program to calculate surface area and volume of cylinder

pi=22/7
height=float(input("Enter Height : "))
radius=float(input("Enter Radian : "))
volume=pi*radius*radius*height
sur_area=((2*pi*radius)*height) + ((pi*radius**2)*2)
print("Volume is : ",volume)
print("Surface Area is : ",sur_area)
