
def default_test(a=10,b=20,c=50,d=40):
    print('a:',a,'b:',b,'c:',c,'d:',d)

default_test()              # will print default values if not given while calling 
default_test(1,2,3,4)       # otherwise the args while calling will be considered
default_test(1,2,3)
default_test(1,2)
default_test(1)
default_test(b=483,c=987)