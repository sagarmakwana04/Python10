# this is called arbitrary arguments in which we can store more than one data value and that data will be stored into *tuple and **dictionery
# the sequence for this args will be *single star first and **double star second

def arb_test(a,b,c,*d,**e):
    print(a,b,c,d,e)

arb_test(1,2,3,4,5,6,7,8,9, x=19,y=29,z=99)