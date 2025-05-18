class Calculator:
    # Overloading (tidak langsung didukung Python, simulasi)
    def add(self, a, b, c=None):
        if c:
            return a + b + c
        return a + b
    
    # Overriding
    def show_result(self):
        print("Calculation done")

class ScientificCalculator(Calculator):
    def show_result(self):  # Overriding
        print("Scientific result")

# Usage
calc = ScientificCalculator()
print(calc.add(1, 2))     # Output: 3 (overloading)
calc.show_result()        # Output: Scientific result (overriding)