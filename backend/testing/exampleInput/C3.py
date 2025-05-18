class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Menghitung luas persegi panjang."""
        return self.length * self.width

    def perimeter(self):
        """Menghitung keliling persegi panjang."""
        return 2 * (self.length + self.width)

    def is_square(self):
        """Memeriksa apakah ini adalah persegi."""
        return self.length == self.width

    def display_properties(self):
        """Menampilkan informasi tentang persegi panjang ini."""
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        if self.is_square():
            print("This is a square.")
        else:
            print("This is not a square.")
