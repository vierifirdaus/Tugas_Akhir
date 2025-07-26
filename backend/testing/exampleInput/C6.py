class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} added to your balance.")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} deducted from your balance.")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be positive.")

    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        # Memanggil constructor dari class induk
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Metode khusus untuk menambahkan bunga ke saldo"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to your balance.")
