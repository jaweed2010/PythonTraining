from BankingApplication.BankingApp.Users.Person import Person


class Customer(Person):
    def __init__(self, name, age, address, customer_id):
        super().__init__(name, age, address)
        self._customer_id = customer_id
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def display_info(self):
        print(f"CUSTOMER INFO:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Address: {self._address}")
        print(f"Customer ID: {self._customer_id}")
        print()

    def display_accounts(self):
        print("ACCOUNTS:")
        for account in self._accounts:
            print(account)