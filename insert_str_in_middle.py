# Function to insert a string in middle of string

def inser_str_middle(s,word):
    return s[:2]+word+s[2:]

print(inser_str_middle('[[]]','Python'))
print(inser_str_middle('{{}}','php'))
print(inser_str_middle('<<>>',"html"))
