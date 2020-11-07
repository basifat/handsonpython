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

    def __str__(self):
        return f"Customer {self.customer_name} with account no {self.account_no}."
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return ("Withdraw Successful",self.balance) 

        return ("Insufficient funds", self.balance)

    def deposit(self,amount):
        self.balance += amount
        return self.balance


# Insufficient funds, 30
# Withdraw Successful, 50







john = Bank("John Bosco", "1")
print(john)

#first withdraw attempt
balance =john.withdraw(50.00)
print(balance)

#first deposit attempt
deposited = john.deposit(10.00)
print(deposited)

#next withdraw attempt
balance =john.withdraw(50.00)
print(balance)


