# #class on Thursday 27/08/2020

class BitcoinBank:
    
    def __init__(self, customer_name, account_no):
        self.customer_name= customer_name
        self.bit_address = account_no
        self.balance = 0

    def __str__(self):
        return f"Customer {self.customer_name} with account no {self.bit_address}."

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance)        
            
        return ("Insufficient funds", self.balance)
        
# Deposit money into a bank account: go to the bank to add to the existing balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance

owner_crypto = BitcoinBank("Tunde", 8888)
print(owner_crypto)
#output is Customer Tunde with bit address 8888.

#to print the balance
print(owner_crypto.balance)#output is 0

#withdraw
withdrawal = owner_crypto.withdraw(50)
print(withdrawal) # output is ('Insufficient funds', 0)

#deposit
balance = owner_crypto.deposit(100)
print(balance)#output is 100

#withdrawing again
withdrawal = owner_crypto.withdraw(80)
print(withdrawal)#output is ('Withdraw Successful', 20)

#withdrawing
withdrawal = owner_crypto.withdraw(120)
print(withdrawal)#output is ('Insufficient funds', 20)




class ArgosWallet:

    def __init__(self, customer_name, account_no):
        self.customer_name= customer_name
        self.wallet_no = account_no
        self.balance = 0

    def __str__(self):
        return f"Customer {self.customer_name} with account {self.wallet_no}."
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance)        
            
        return ("Insufficient funds", self.balance)
        
# Deposit money into a bank account: go to the bank to add to the existing balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance

david_wallet = ArgosWallet('David', 2468)
print(david_wallet)#output is Customer David with wallet number 2468.

withdraw_money = david_wallet.withdraw(1000)
print(withdraw_money)# output is ('Insufficient funds', 0)

deposit_money = david_wallet.deposit(5000)
print(deposit_money)#output is 5000

withdraw_money = david_wallet.withdraw(1000)
print(withdraw_money)#output is ('Withdraw Successful', 4000)




#A generic class that can be used for various university


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
        
# Deposit money into a bank account: go to the bank to add to the existing balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance

class UniGlasgow(GenericUniversityWallet):
    pass

class UniLeeds(GenericUniversityWallet):
    pass

class UniManchester(GenericUniversityWallet):
    pass

class UniAberdeen(GenericUniversityWallet):
    pass

#create an instance of uniglsgow
uni_glasgow = UniGlasgow("Toyin", 888)
print(uni_glasgow)#output is Student Toyin with wallet number 888.

uni_leeds = UniLeeds("Kemi", 889878)
print(uni_leeds)#output is Student Kemi with wallet number 889878

uni_manchester = UniManchester("Andre", 888)
print(uni_manchester) #output is Student Andre with wallet number 888.

uni_aberdeen = UniAberdeen("Shola", 235)
print(uni_aberdeen)#output is Student Shola with wallet number 235.

#Assignment
# 
# #create a generic bank class that allows us to create the other types of bank that we had before
#2. We now have a generic university. we then need to have a method for each university that allows
# a student to print the name of their university
#i.e uni_glasgow.get_university_name()-> "hey, this is the University of Glasgow"
#uni_manchester.get_university_name()->"Hey, this is the University of Machester"

#3 Metaclasses -> create an abstract class that require the user or callee to define both deposit and withdraw methods
# require me to define a method called deposit
#withdraw
    def deposit():

    def withdraw()





