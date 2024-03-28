class BankAccount:
    def __init__(self,amount):
        self.amount=amount

    def deposit(self,amnt):
        self.amount=self.amount+amnt

    def withdraw(self,amnt):
        if self.amount-amnt < 0:
            return "insufficient balance"
        else:
            self.amount=self.amount-amnt

add = BankAccount(100)

