class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < 0:
            print ("Insufficient funds: Charging a $5 fee ")
            self.balance -= 5
        else:
            self.balance -= amount
            # print(self.balance)
        return self

    def display_account_info(self):
        print (f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance *= (self.int_rate)
        if self.balance >=0:
            return self
        else:
            pass

## Accounts
Account1 = BankAccount (1.01, 1000)
Account2 = BankAccount (1.01, 2000)

## Transactions
Account1.deposit(100).deposit(200).deposit(200).withdraw(500).yield_interest().display_account_info()
Account2.deposit(400).deposit(100).withdraw(350).withdraw(700).withdraw(50).withdraw(100).yield_interest().display_account_info()
