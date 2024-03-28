from BankingApplication.BankingApp.Accounts.Account import Account


class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount <=0:
            print("Invalid amount for withdrawal.\n")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self._balance}")
        else:
            print("Insufficient funds for withdrawal.")