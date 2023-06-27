# demo of banking system 
# openAcc, dip, withd, checkb
# class, function and variables, object, while loop choices

class Bank:
    def openAccount(self,cname,acno,balance):
        self.c=cname
        self.a=acno
        self.b=balance
        print(f"Hello {self.c}, Your Account Number {self.a} Is Opened With {self.b} Rs.")
    def diposit(self,amount):
        self.b=self.b+amount
    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            print(f"You Need Another {amount-self.b} Rs.")
    def checkBalance(self):
        print(f"Your Current Balance is {self.b}")

b1=Bank()
cname=input("Enter Your Name : ")
acno=int(input("Enter Your Account Number : "))
balance=int(input("Enter Initial Balance : "))
b1.openAccount(cname,acno,balance)

while True:
    print("1. Diposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice=int(input("Enter Your Choice : "))

    if choice==1:
        amount=int(input("Enter Diposit Amount : "))
        b1.diposit(amount)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkBalance()
    else:
        print("Thank You For Visiting Our Services, Have A Good Day.")
        break
