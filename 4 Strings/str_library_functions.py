# STRING DEMO of its library function in python

s = "Python programming"

# quite tuff : 
print("7.", s.count("o"))        # this will count how much o comes in given string
print("8.", s.count("o", 8))     # if 8 is gives then it will check from index 8 how much o comes     
print("13", s.center(40, "~"))        # this will first occupy space for 40 letter and then it will put given string into center and then given command equally both side     
print("14.", s.index("o", 3))           # this will give index value of 'o' after 3
print("27.", "Hello".replace("l", "w"))     # will replace the given letter to the given letter
print("sagar".replace("a","o"))
print("29.", s.title())             # title will upper all first letters of all words in given str
print("welcome to the world of python programming".title())     # this will upper all first letter of all words

print("2.", s.capitalize())       # capitalize only first letter of given string
print("3.", s.casefold())          # it can lower case all letters
print("4.", s.upper())            # upper case all letters
print("5.","PYTHON".lower())     # lower case all letter
print("9.", s.count("P",0))       # P after 0 comes 1 time but after 1 zero time
print("10.", s.endswith("ing"))      # boolean function checks whether the given string ends from given condition or not output in boolean function will be True or False
print("11.", s.startswith("Py"))     # boolean function checks whether the given string starts from given condition or not
print("12.", s.find("h"))            # finds the index value of given letter
print("14.", s.index("o"))             # it will give that 0 comes at which index
print("15.", "abc123".isalnum())        # alnum, alphanumberic = 'A-Z or a-z or 0-9' 
print("16.", "abc".isalpha())        # is alpha checks only = 'A-Z or a-z'
print("17.", s.islower())             # checks is all letters are lower or not
print("18.", "PYTHON".isupper())        # checks is all letters are upper or not
print("19.", s.isnumeric())       
print("20.", "123".isnumeric())       #is All letters are numberic or not
print("21.", " ".isspace())          # this will only check is the string is "ONLY" space or not 
print("22.", " py PRO ".isspace())         # if any other char is inside will output as false     
print("23.", "Python Programming Inbuilt Library Functions".istitle())      # is first letter of all word capital or not
print("24.", "Python programming inbuilt Library functions".istitle())      # is first letter of all word capital or not
print("25.", "PYThoN".lower())           # will lower all letters
print("26.", "programming".upper())      # upper all letters
print("28.", "Jay Sachidanand".swapcase())      # will swap the upper to lower and vice versa
print("30.", "1234".isdecimal())        # checks '0-9'
print("31.", "123".isdigit())       # checks '0-9'
print("32.", "fjsthe5348--''';rlwe'q3421@##%!#%$#^^6660*()*)(*463271657)".isprintable())
print("32.", "fjsthe5348--''';rlwe'q3421@##%!#%$#^^6660*()*)(*463271657)  \n".isprintable())        # is printable or not, string with \n is not printable
print("33.", "http://python.org".removeprefix("http://"))     # this can remove the given prefix which starts from left --> first or positive
print("34.", "http://python.org".removesuffix(".org"))     # this can remove the given prefix which starts from right <-- last or negative
print("35.", s.join("12"))      # this will join the given condition into space of string
print("36.", s.partition(" "))      #this will create tuple and separates given string
print("37.", s.split(" "))          # this will create list and separates given string
txt = "9"
print("38.", txt.zfill(10))     # first it will occupy 5 spaces and then will put given argument at last and rest of place 0