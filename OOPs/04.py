'''
Create a BankAccount class that stores an account holder's name and balance. Add instance methods to deposit money, withdraw money and display the balance. Do not allow withdrawal greater than the available balance
'''
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdrawl(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawl successfull!!")
        else:
            print("Insufficient balance!!")
    def display_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Balance : {self.balance}")

name = input("Enter account holder's name: ")
balance = float(input("Enter the initial balance: "))

account = BankAccount(name, balance)

amount = float(input("Enter amount to deposit: "))
account.deposit(amount)

amount = float(input("Enter amount to withdraw: "))
account.withdraw(amount)

account.display_balance()