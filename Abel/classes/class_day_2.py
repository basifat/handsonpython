## Write a class that depicts a bank.
## It should allow the following(note that a negative balance is not allowed)
## Create a bank customer
## Withdraw money from a bank customer account
## Deposit money into a bank account

## Transfer money from one customer of the bank to another customer of the bank. i.e John sends 50 to Lee
## Keep a record/ledger of every deposit and withdrawal for a customer. i.e John withdraws 50, then later deposits 200, 
# we should return a list that has for example [John withdrew 50, John deposited 200]
## Add a method that returns the ledger or record of deposits and withdrawals.


class Bank:

    def __init__(self, customer_name, account_no):
        self.customer_name= customer_name
        self.account_no = account_no
        self.balance = 0
        self.ledger =[]
        
        
    def withdraw(self, amount):
        if self.balance>= amount:
            self.balance = self.balance- amount
            print("Withdraw Successful",self.balance)
            self.ledger.append(f"{self.customer_name} withdrew {amount} ")
            return self.ledger
        else:
            return ("Insufficient Funds", self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.ledger.append(f" {self.customer_name} deposited {amount}")
        return self.ledger
        

    
    def transfer(self, amount, recipient):
        if self.balance>= amount:
            self.balance = self.balance- amount
            recipient.balance += amount
            return (f"Transfer Successfull you transfered {amount} pounds")
        else:
            return ("Insufficient Funds", self.balance)
        
       

# Deposite
john = Bank("John Bosco", "648")
deposited =john.deposit(500)
print(deposited)

#Transfer from one Bank Customer to another Account
jane = Bank("jane", "444")
print(john.transfer(50 ,jane))

# Withdraw
withdrawal = john.withdraw(100)
print(withdrawal)
