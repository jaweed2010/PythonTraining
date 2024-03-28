from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit of {amount} successful. New balance: {self._balance}\n")
        else:
            print("Invalid amount for deposit.\n")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __str__(self):
        return f"Account Number: {self._account_number}\nBalance: {self._balance}\n"

