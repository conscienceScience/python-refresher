import numpy as np

class Bank:
    def __init__(self, name, acc_num):
        self.balance = 0
        self.name = name
        self.account_number = acc_num
    
    def withdraw(self, amt):
        if(amt>=0 and self.balance>=amt):
            self.balance = self.balance - amt
            return self.balance
        elif(amt>=0 and self.balance<amt):
            print("You do not have enough money in your balance.")
            return "error"
        else:
            print("Error, can't withdraw negative amount.")
            return 'error'

    def deposit(self, amt):
        if(amt>=0):
            self.balance = self.balance+amt
            return self.balance
        else:
            print("Error, can't deposit negative amount.")
            return 'error'
    
    def print_current_balance(self):
        print(self.balance)
        return self.balance

    def get_name(self):
        return self.name
    
    def get_acc_num(self):
        return self.account_number