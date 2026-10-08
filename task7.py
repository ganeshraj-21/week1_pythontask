class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


account = BankAccount("Arun", 10000)

account.deposit(5000)
account.withdraw(20000)

account.display_balance()