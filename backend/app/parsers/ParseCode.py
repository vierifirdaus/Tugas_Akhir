import ast
def parse_code(code):
    tree = ast.parse(code)
    result = {'class': [], 'function': [], 'main': ''}

    main_code = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            result['function'].append(node.name)
        elif isinstance(node, ast.ClassDef):
            class_data = {
                'classname': node.name,
                'method': []
            }
            for class_node in node.body:
                if isinstance(class_node, ast.FunctionDef):
                    class_data['method'].append(class_node.name)
            result['class'].append(class_data)
        else:
            main_code.append(ast.unparse(node))

    result['main'] = "\n".join(main_code)
    return result

code = r"""
# Class Induk
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
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to your balance.")

def main():

    def a() :
        print("This is a test function inside main.")
    print("Creating a bank account for Alice.")
    alice_account = BankAccount("Alice", 1000)
    print(f"Initial balance: {alice_account.get_balance()}")
    alice_account.deposit(500)
    alice_account.withdraw(200)
    print(f"Final balance: {alice_account.get_balance()}")
    print("\nCreating a savings account for Bob.")

main()

for i in range(5) :
    print("This is a test for the C6.py file, iteration:", i + 1)
"""

parsed_data = parse_code(code)
print(parsed_data)