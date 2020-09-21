##Friday 28/08/2020

from abc import ABC, abstractmethod

class GenericUniversityWallet(ABC):
    balance = 0


    def __init__(self, student_name, wallet_no):
        self.wallet_no = wallet_no
        self.student_name = student_name
        

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError

    
#shared method
    def transfer(self, amount):
        return amount

class UniGlasgow(GenericUniversityWallet):
    #individual or specific method. this are not shared
    def deposit(self, amount):
        self.balance += amount
        return f"University of Glasgow wallet balance of {self.balance}"

    def withhdraw(self, amount):
        pass

class UniManchester(GenericUniversityWallet):

    def deposit(self, amount):
        self.balance += amount
        return f"Hallo, manchester uni wallet balance of {self.balance}"


class UniLeeds(GenericUniversityWallet):

    def deposit(self, amount):
        self.balance += amount
        return f"Hallo, Leeds uni wallet balance of {self.balance}"


        
# john = Bank("John", 112)
# print(john)

uni_glasgow = UniGlasgow('Abel', 113)
print(uni_glasgow.deposit(10))

uni_manchester = UniManchester('Tunde',127)
print(uni_manchester.deposit(10))

print(uni_manchester.transfer(10))


#Assignment
#1 Add a transfer method which ia an abstract method to the GenericUniversityWallet class
#2 Specify how each child class i.e university implements its transfer method
#somebody might transfer and send emails and another might send something else
 #you can add a print to say email sent successfully
    @abstractmethod
    def transfer(self, amount):

#next topic: sper, dunder, private variables etc


