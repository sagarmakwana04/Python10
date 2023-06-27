a=(input("Enter Value:"))
print(f"Multiplication Table of {a} is:")

try:        # code will always be inside of try
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("End of Program")