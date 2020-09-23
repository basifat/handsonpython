from abc import ABC, abstractmethod 

class GenericBank(ABC):
    """ 
    This class defines methods that allow other classes to implement 'withdrawal' and 'deposit' 
    but enforces the 'bank_transfer' method to be implemented by sub classes

    """


    def withdraw(self, amount):
        raise NotImplementedError
        
    
    def deposit(self,amount):
        raise NotImplementedError
    
    @abstractmethod
    def bank_transfer(self, sender, receiver):
        pass
        


class NordeaBank(GenericBank):
    
    def __init__(self,  customer_name,account_no):
        self.customer_name= customer_name
        self.account_no = account_no
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance) 
        else:
            return ("Insufficient funds", self.balance)

    def deposit(self,amount):
        self.balance += amount
        return self.balance

     
    def bank_transfer(self, amount, recipient):
        self.withdraw(amount)
        recipient.deposit(amount)
        return self.balance





