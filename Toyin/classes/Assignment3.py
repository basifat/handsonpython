# Assignment after class_day_2.py

## Transfer money from one customer of the bank to another customer of the bank. i.e John sends 50 to Lee
## Keep a record/ledger of every deposit and withdrawal for a customer. i.e John withdraws 50, then later deposits 200, 
# we should return a list that has for example [John withdrew 50, John deposited 200]
## Add a method that returns the ledger or record of deposits and withdrawals.


class Bank:
    
    def __init__(self, customer_name, account_no):
        self.customer_name= customer_name
        self.account_no = account_no
        self.balance = 0


#method that shows the customer's name and account number
    def __str__(self):
        return f"Customer {self.customer_name} with account no {self.account_no}."

# Withdraw money from a bank customer account
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return f"{self.customer_name} withdrew {amount}."
        return ("Insufficient funds", self.balance)# this will return that it wasn't successful and the current balance
       

# Deposit money into a bank account: go to the bank to add to the existing balance
    def deposit(self,amount):
        self.balance += amount
        return f"{self.customer_name} deposited {amount}."

# Transfer money from one customer of the bank to another customer of the bank. i.e John sends 50 to Lee
    def transfer(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.balance -= amount
        return f"transfer successful, {self.receiver} received {amount}."




john = Bank("John Bosco", "1")
print(john)

#deposit attempt
deposited = john.deposit(200)
print(deposited)

#withdraw attempt
withdrawal =john.withdraw(50)
print(withdrawal)

transfered  = john.transfer('John Bosco', 'Lee', 50)
print(transfered)