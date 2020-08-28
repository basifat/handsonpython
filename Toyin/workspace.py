from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
        super().__init__()

    @abstractmethod
    def money(self):
        pass

class TakeOutMoney(AbstractClass):
    def money(self):
        return ("withdraw Successful", self.balance)

class Deposit(AbstractClass):
    def money(self):
        return "Milk only "+ str(self.balance) + " times or more each day"

food = 3    
mom = TakeOutMoney(food)
#print("moms ----------")
print(mom.money())

infant = Deposit(food)
#print("infants ----------")
print(infant.money())