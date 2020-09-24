from abc import ABC, abstractmethod 

class Faculties:
    """ This class defines the name and faculty of a university"""

    def __deen(self):
        return "Mr Barry"

    def list_faculties(self,):
        name=self.__deen()
        lst = ["Biology","Pharmacy"]
        lst.append(name)
        return lst

    def public_deen(self):
        return self.__deen()

    def get_deen(self):
        return "Mr Barry White"


class UniversityOfWales(Faculties):
    """ Inherits Properties of faculty class"""
    def get_deen(self):
        name=super().get_deen()
        return "phd " + name


class GenericUniversityWallet(ABC):
    """ 
    The abstract class defines interface that will can be implemented according to 
    how each subclass wants to implement the methods.
    """
    uni_name = ""
   
    def print_uni_name(self):
        return f" Hey this the {self.uni_name}"


    def deposit(self, amount):
        """ deposit funds to owner's account""" 
        raise NotImplementedError 

    def withdraw(self, amount):
        """ withdraw funds from owner's account"""
        raise NotImplementedError
    
    @abstractmethod
    def bank_transfer(self, amount, recipient):
        """ transfer funds from one account to another"""
        pass


class UniGlasgow(GenericUniversityWallet):
    """ inherits properties of the super class """

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


class UniLeeds(UniGlasgow):
    """ implements the abtract method 'bank_transfer' from the super class """
    
    def send_mail(self):
        return "check email for reference number"

    def bank_transfer(self, amount, recipient):
        self.balance=self.withdraw(amount)
        recipient.balance =recipient.deposit(amount)
        return (f"{self.student_name} transfered {amount} pounds, balance is {self.balance} {self.send_mail} " )


