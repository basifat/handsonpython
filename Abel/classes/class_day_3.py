from abc import ABC, abstractmethod 
class Bank(ABC):

    def withdraw(self, amount):
        raise NotImplementedError
        
    
    def deposit(self,amount):
        raise NotImplementedError
    
    @abstractmethod
    def bank_transfer(self, sender, receiver):
        pass
        


class NordeaBank(Bank):
    
    def __init__(self,  customer_name,account_no):
        self.customer_name= customer_name
        self.account_no = account_no
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance) 

        return ("Insufficient funds", self.balance)

    def deposit(self,amount):
        self.balance += amount
        return self.balance

     
    def bank_transfer(self, amount, recipient):
        self.withdraw(amount)
        recipient.deposit(amount)
        return self.balance


bank_1= NordeaBank("Joe",234)
send_funds=bank_1.deposit(50)
print(send_funds)

bank_2= NordeaBank("mat",678)
print(bank_1.bank_transfer(20, bank_2))




class Faculties:

    __deen_age =90
    deen_age = __deen_age

    def __deen(self):
        return "Mr Banjo"

    def list_faculties(self,):
        name=self.__deen()
        lst = ["Agric","Pharmacy"]
        lst.append(name)
        return lst

    def public_deen(self):
        return self.__deen()

    def get_deen(self):
        return "Mr Banjo Ojamila"

department = Faculties()
print(department.list_faculties())

class UniIbadanWallet(Faculties):
    def get_deen(self):
        name=super().get_deen()
        return "phd " + name

uni_wallet = UniIbadanWallet


#1. Add a transfer method which is an abstract method to the GenericUniversityWallet class
#2. Specify how each child class i.e university of manchester implments its transfer method 
from abc import ABC, abstractmethod 
class GenericUniversityWallet(ABC):
    uni_name = ""
   
    def print_uni_name(self):
        return f" Hey this the {self.uni_name}"


    def deposit(self, amount):
        raise NotImplementedError 

    def withdraw(self, amount):
        raise NotImplementedError
    
    @abstractmethod
    def bank_transfer(self, amount, recipient):
        pass


class UniGlasgow(GenericUniversityWallet):

    def __init__(self, student_name, account_no):
        self.student_name = student_name
        self.wallet_no = account_no
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance

        return ("Insufficient funds, top up balance", self.balance)

    def bank_transfer(self, amount, recipient):
        self.balance=self.withdraw(amount)
        recipient.balance =recipient.deposit(amount)
        return (f"{self.student_name} transfered {amount} pounds, your new balance is {self.balance}")

bety= UniGlasgow("Betty", 444)
print(bety.deposit(100))
kunle =UniGlasgow("Kunle", 332)
print(bety.bank_transfer(80, kunle))

class UniLeeds(UniGlasgow):
    

    def bank_transfer(self, amount, recipient):
        self.balance=self.withdraw(amount)
        recipient.balance =recipient.deposit(amount)
        return (f"{self.student_name} transfered {amount} pounds, balance is {self.balance}, check email for reference number" )

ugo = UniLeeds("Ugo", 222)
print(ugo.deposit(500))

tayo = UniLeeds("tayo", 890)
print(ugo.bank_transfer(500,tayo))




        









    

    

    




