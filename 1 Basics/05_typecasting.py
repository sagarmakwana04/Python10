"""
There are 2 types of typecasting
3. Explicit Conversion (done via developer or programmer)
which can be done by int(), float(), hex(), oct(), str(), etc
2. Implicit Conversion (done by python)
like if we add 2+3.2 then python will internally make then float and will give answer in float
"""
#Example of Explicit TypeCasting
a = "11"
b = "22"
print(a+b)              # this will concate the string
print(int(a)+int(b))    # this will convert string as int and then addition of int


#Example of Impicit TypeCasting
c = 2
d = 3.2
print(c+d)
