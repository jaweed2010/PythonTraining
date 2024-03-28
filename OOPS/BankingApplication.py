from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    @abstractmethod
    def display_info(self):
        pass


class Customer(Person):
    def __init__(self, name, age, address, customer_id):
        super().__init__(name, age, address)
        self._customer_id = customer_id
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def display_info(self):
        print(f"Customer Information:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Address: {self._address}")
        print(f"Customer ID: {self._customer_id}")

    def display_accounts(self):
        print("Accounts:")
        for account in self._accounts:
            print(account)


class Employee(Person):
    def __init__(self, name, age, address, employee_id, role):
        super().__init__(name, age, address)
        self._employee_id = employee_id
        self._role = role

    def display_info(self):
        print(f"Employee Information:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Address: {self._address}")
        print(f"Employee ID: {self._employee_id}")
        print(f"Role: {self._role}")


class Account(ABC):
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit of {amount} successful. New balance: {self._balance}")
        else:
            print("Invalid amount for deposit.")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __str__(self):
        return f"Account Number: {self._account_number}\nBalance: {self._balance}"


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self._balance}")
        else:
            print("Insufficient funds for withdrawal.")


class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self._balance}")
        else:
            print("Insufficient funds for withdrawal.")

    customer1 = Customer("John Doe", 30, "123 Main St", "C123")
    customer1.display_info()

    savings_account = SavingsAccount("S12345", 1000)
    customer1.add_account(savings_account)

    customer1.display_accounts()

    savings_account.deposit(500)
    savings_account.withdraw(200)
    savings_account.withdraw(2000)

    employee1 = Employee("Jane Smith", 25, "456 Elm St", "E001", "Bank Teller")
    employee1.display_info()
