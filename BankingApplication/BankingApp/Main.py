from BankingApplication.BankingApp.Users.Customer import Customer
from BankingApplication.BankingApp.Users.Employee import Employee
from BankingApplication.BankingApp.Accounts.SavingsAccount import SavingsAccount
from BankingApplication.BankingApp.Accounts.CheckingAccount import CheckingAccount

while True:
    customer1 = None
    employee1 = None
    print("Welcome to The Bank.")
    print("Please let us now how you want us to serve you.")
    print("Just enter the first letter(in small case) of the service from below options and press Enter.")
    print("- Generate profile.")
    print("- Create Account.")
    print("- Transact.")
    char = input()
    if char == 'g':
        print("Select the relevant profile options. Just type the first letter in small case and press Enter.")
        print("- Customer")
        print("- Employee")
        opt = input()
        if opt == 'c':
            customer1 = Customer("John Doe", 30, "123 Main St", "C123")
            print("Customer profile created")
            customer1.display_info()
        if opt == 'e':
            employee1 = Employee("Jane Smith", 25, "456 Elm St", "E001", "Bank Teller")
            print("Employee profile created")
            employee1.display_info()

    elif char == 'c':
        customer1 = Customer("John Doe", 30, "123 Main St", "C123")
        print(
            "Select the relevant account type you want to create form below options. Just type the first letter in small case and press Enter.")
        print("- Savings Account")
        print("- Checking Account")
        opt = input()
        if opt == 's':
            savings_account = SavingsAccount("S12345", 1000)
            customer1.add_account(savings_account)
            print("Savings account created")
            customer1.display_accounts()
        if opt == 'c':
            checking_account = CheckingAccount("C12345", 2000)
            customer1.add_account(checking_account)
            print("Checking account created")
            customer1.display_accounts()

    elif char == 't':
        customer1 = Customer("John Doe", 30, "123 Main St", "C123")
        savings_account = SavingsAccount("S12345", 1000)
        while True:

            print(
                "Please select the transaction you would like to perform. Just type the first letter in small case and press Enter.")
            print("If you would like to end the session just type 'e' and press Enter.")
            print("- Deposit")
            print("- Withdraw")

            opt = input()
            if opt == 'e':
                print("Thank you for banking with us!\n")
                break

            elif opt == 'd':
                print("Please enter the amount to be deposited.")
                amt = int(input())
                savings_account.deposit(amt)

            elif opt == 'w':
                print("Please enter the amount to be withdrawn.")
                amt = int(input())
                savings_account.withdraw(amt)
