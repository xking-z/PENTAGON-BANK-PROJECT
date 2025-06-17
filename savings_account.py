# savings_account.py

class SavingsAccount:
    def __init__(self, balance=0.0, interest_rate=0.01):
        """Initialize a new Savings Account.

        Args:
            balance (float): Starting balance for the account. Default is 0.0.
            interest_rate (float): Annual interest rate. Default is 1%.
        """
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        """Deposit money into the savings account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the savings account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def add_interest(self):
        """Add interest to the account based on current balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")

    def get_balance(self):
        """Return the current balance."""
        return self.balance
