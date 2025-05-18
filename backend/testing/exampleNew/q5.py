class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # Validasi
            self.__balance -= amount
            return amount
        raise ValueError("Invalid amount")

# Usage
account = BankAccount(1000)
account.withdraw(500)  # Output: 500