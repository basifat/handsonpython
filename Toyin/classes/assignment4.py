#Assignment
# 
#1.create a generic bank class that allows us to create the other types of bank that we had before
#2. We now have a generic university. we then need to have a method for each university that allows
# a student to print the name of their university
#i.e uni_glasgow.get_university_name()-> "hey, this is the University of Glasgow"
#uni_manchester.get_university_name()->"Hey, this is the University of Machester"

#3 Metaclasses -> create an abstract class that require the user or callee to define both deposit and withdraw methods
# require me to define a method called deposit
#withdraw

# 1.1
class GenericBank:
    
    def __init__(self, customer_name, account_no):
        self.customer_name= customer_name
        self.account_no = account_no
        self.balance = 0


#method that shows the customer's name and account number
    def __str__(self):
        return f"Customer {self.customer_name} with account no {self.account_no}."

 # Withdraw money from a bank customer account
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance) 
        return ("Insufficient funds", self.balance)


# Deposit money into a bank account: go to the bank to add to the existing balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance

class Lloyds(GenericBank):
    pass

class Natwest(GenericBank):
    pass

class Santander(GenericBank):
    pass


lloyds_customer = Lloyds("Toyin", 888)
print(lloyds_customer)

natwest_customer = Natwest("Jimmy", 222)
print(natwest_customer)

santander_customer = Santander("Toyosi", 333)
print(santander_customer)


#2. We now have a generic university. we then need to have a method for each university that allows
# a student to print the name of their university
#i.e uni_glasgow.get_university_name()-> "hey, this is the University of Glasgow"
#uni_manchester.get_university_name()->"Hey, this is the University of Machester"

class GenericUniversityWallet:

    def __init__(self, student_name, account_no):
        self.student_name= student_name
        self.wallet_no = account_no
        self.balance = 0

    def __str__(self):
        return f"Student {self.student_name} with wallet number {self.wallet_no}."
    
   
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance)        
            
        return ("Insufficient funds", self.balance)
        

    def deposit(self,amount):
        self.balance += amount
        return self.balance

#print name of university

    def print_university(self, uniname):
        self.uniname = uniname
        return f"Hey, this is the {self.uniname}."


class UniGlasgow(GenericUniversityWallet):
    pass

class UniLeeds(GenericUniversityWallet):
    pass

class UniManchester(GenericUniversityWallet):
    pass

class UniAberdeen(GenericUniversityWallet):
    pass

uni_manchester = UniManchester("Samuel", 888)
print(uni_manchester)

student_uni = uni_manchester.print_university('University of Manchester')
print(student_uni)

uni_glasgow = UniGlasgow("Toyin", 567)
print(uni_glasgow)

student_uni_2 = uni_glasgow.print_university('University of Glasgow')
print(student_uni_2)




#3 Metaclasses -> create an abstract class that require the user or callee to define both deposit and withdraw methods
# require me to define a method called deposit
#withdraw

