#Assignment from class_day_4.py*********************COMPLETE
##Friday 28/08/2020
#1 Add a transfer method which is an abstract method to the GenericUniversityWallet class
#2 Specify how each child class i.e university implements its transfer method
#somebody might transfer and send emails and another might send something else
 #you can add a print to say email sent successfully
    # @abstractmethod
    # def transfer(self, amount):

#next topic: sper, dunder, private variables etc


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

    @abstractmethod
    def transfer(self, amount):
        pass

class UniGlasgow(GenericUniversityWallet):

    def deposit(self, amount):
        self.balance += amount
        return f"University of Glasgow wallet balance of {self.balance}"

    def withhdraw(self, amount):
        pass
        
    def transfer(self, amount, email):
        self.email = email
        self.balance -= amount
        return f"transfer successful with email sent to, {self.email} for {amount}."


class UniManchester(GenericUniversityWallet):

    def deposit(self, amount):
        print(amount)

    def withdraw(self, amount):
        print(amount)
        
    def transfer(self, amount, email):
        self.email = email
        self.balance -= amount
        return f"transfer successful with email sent to, {self.email} for {amount}."
        
        
john = UniGlasgow("Deborah", "1")
print(john)

transferred = john.transfer(50, 'tty@yahoo.com')
print(transferred)


