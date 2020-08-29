# Inheritance 
# Object orientation

#1. Bank that allows transfer of bitcoin
#2 . Bank that allows transfer of online Voucher

# Real world Fiat
class Bank:
    
    def __init__(self, customer_name, account_no):
        self.customer_name= customer_name
        self.account_no = account_no
        self.balance = 0

    def __str__(self):
        return f"Customer {self.customer_name} with account no {self.account_no}."
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance) 

        return ("Insufficient Funds", self.balance)

    def deposit(self,amount):
        self.balance += amount
        return self.balance


    

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

        return ("Insufficient Funds", self.balance)

    def deposit(self,amount):
        self.balance += amount
        return self.balance

# owner_crypto = BitcoinBank("Tunde", 77777)
# print(owner_crypto)

# print(owner_crypto.balance)
# withdrawal = owner_crypto.withdraw(50)
# print(withdrawal)

# balance = owner_crypto.deposit(100)
# print(balance)

# withdrawal = owner_crypto.withdraw(120)
# print(withdrawal)


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

        return ("Insufficient Funds", self.balance)
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance

# david_wallet = ArgosWallet("David", 2468)
# print(david_wallet)

# withdraw_money = david_wallet.withdraw(1000)
# print(withdraw_money)

# deposit_money = david_wallet.deposit(5000)
# print(deposit_money)

# withdraw_money = david_wallet.withdraw(1000)
# print(withdraw_money)

class GenericUniversityWallet:

    def __init__(self, student_name, account_no):
        self.student_name= student_name
        self.wallet_no = account_no
        self.balance = 0

    def __str__(self):
        return f"Student {self.student_name} with great wallet number {self.wallet_no}."
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance) 

        return ("Insufficient Funds", self.balance)
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance


class UniAberdeen(GenericUniversityWallet):
    pass


class UniManchester(GenericUniversityWallet):
    pass


class UniLeeds(GenericUniversityWallet):
    pass
      

class UniGlasgow(BankAbstract):
    pass


uni_glasgow=UniGlasgow("Toyin", 888)
print(uni_glasgow)

uni_manchester=UniManchester("Andre", 444)
print(uni_manchester)


#1. Create a generic bank class that allows us to create the other types of bank that we had before.
#2. We now have a generic university. We then need to have a method for each univeristy that allows 
#   a student to print the name of their university
# i.e uni_glasgow.get_university_name() -> "Hey, this is the University of Glasgow"
# uni_manchester.get_university_name() -> "Hey, this is the University of Manchester"

#3. Metaclasses -> Create an abtsract class that requires the user or callee to define both deposit and withdraw methods.
