class PrimeCalculator:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        """Periksa apakah angka adalah bilangan prima."""
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True