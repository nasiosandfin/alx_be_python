class BankAccount:
    """A simple bank account class with deposit, withdraw, and balance display methods."""

    def __init__(self, initial_balance=0):
        # Encapsulation: account_balance is private
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Returns True if successful, False otherwise."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        """Print the current balance in a user-friendly format with two decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")


    