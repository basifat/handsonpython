from abc import ABC, abstractmethod


#1. Add a transfer method which is an abstract method to the GenericUniversityWallet class
#2. Specify how each child class i.e university of manchester implments its transfer method 


class GenericUniversityWallet(ABC):
    balance = 0

    def __init__(self, student_name, wallet_no):
        self.wallet_no = wallet_no
        self.student_name = student_name

    def deposit(self, amount):
        raise NotImplementedError 

    def withdraw(self, amount):
        raise NotImplementedError



class UniGlasgow(GenericUniversityWallet):

    # indiviaul or specific methods
    
    def deposit(self, amount):
        self.balance += amount
        #semnd email

        return f"University of Glasgos wallet balance of {self.balance}"

    def withdraw(self, amount):

        pass


class UniManchester(GenericUniversityWallet):
    
    def deposit(self, amount):
        self.balance += amount
        # send sms

        return f"Hallo, manchester Uni wallet balance of {self.balance}"


class UniLeeds(GenericUniversityWallet):
    
    def deposit(self, amount):
        self.balance += amount
        # send courirer letter

        return f"Hallo, Leeds Uni wallet balance of {self.balance}"



# john = Bank('John',112)
# print(john)
uni_glasgow = UniGlasgow('Abel',113)

print(uni_glasgow.deposit(10))

uni_manchester = UniManchester("Tunde", 127)

print(uni_manchester.deposit(10))

print(uni_manchester.transfer(10))

#super 
# dunder
# private  vairables and 




