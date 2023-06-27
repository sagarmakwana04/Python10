
message = "Jsca Python World!"
print(message)

message = "Jsca Python Crash Course World!"
print(message)      # we can change the value of variable at any time and python will always keep track of its current value

message_1 = " "         # valid
# 1_message = " "       # invalid variable variable cant start with number
# msg_1!@ = "asdf"      # invalid variable cant start with special symbols


# print(mesage)     #NameError

"this is a string"
'this is also a string'

s = "This is string in 'python', 'of' "     # if we need single quotation in string then we can store it in double quotation, vice versa
print(s)

name = "saGAR mAkwAna"
print(name.title())
print(name.upper())
print(name.lower())


# fstrings, f=format
f_name = "sagar"
l_name = "makwana"
full_name = f"{f_name} {l_name}"
print(f"Hello, {full_name.title()}!")


# whitespaces
print("Python")
print("\tPython")       # \t will add double tab spaces totol=8 spaces will be added

print("Languages: \nPython\nJavaScript\n")

print("Python : \n\tBasics\n\tif-else,for-while loop\n\tlsit[],tuple(),dict{}\n\tfunction\n\toops\n\ttkinter\n\tmy sql\n\thtml\n\tcss\n\tjavascript\n\tdjango")

fav_lang = "python  "
print(fav_lang.rstrip())        # this will remove the whitespace
print(fav_lang)     # this will not remove this will print the original value whit white space but to remove whitespace permanently we have to assign it as a variable
fav_lang = fav_lang.rstrip()
print(fav_lang)


# remove prefixes
nostarch_url = "https://nostarch.com"
print(nostarch_url)
print(nostarch_url.removeprefix("https://"))
print(nostarch_url)     # this will again print with prefix, so to remove prefit permanently reassign a new variable and print that variable
simple_url = nostarch_url.removeprefix("https://")
print(nostarch_url.removeprefix("https://"))

filename = "https://python_notes.txt"
print(filename.removeprefix("https://"))
print(filename.removesuffix(".txt"))
print(filename)         # to remove suffix permanently new assign variable and then remove
fname=filename.removesuffix(".txt")
print(fname)

famous_person = 'Dada Bhagwan once said, "When there is a will then there is a way."'
print(famous_person)
message = famous_person
print(message)

name2 = "   justin mattew   "
print(name2)
print(name2.lstrip())       # removes left side whitespaces
print(name2.rstrip())       # removes right side whitespaces
print(name2.strip())        # removes both side whitespaces
