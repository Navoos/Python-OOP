"""
BankAccount to manage the bank account for a user
"""


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = (
            account_holder  # Protected: Convention not to modify directly
        )
        self.__balance = initial_balance  # Private: Name mangled, internal state

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid Withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self._account_holder


if __name__ == "__main__":
    my_account = BankAccount("Alice", 1000)
    print(f"Account holder: {my_account.get_account_holder()}")
    print(f"Initial balance: {my_account.get_balance()}")

    my_account.deposit(500)
    my_account.withdraw(1000)
    my_account.withdraw(5000)
