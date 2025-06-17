class Account:
    def _init_(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance