class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        """Menambahkan produk ke keranjang belanja dengan jumlah tertentu."""
        if not isinstance(product, Product):
            raise ValueError("Item yang ditambahkan harus berupa produk.")
        for _ in range(quantity):
            self.items.append(product)
        print(f"Added {quantity} x {product.get_name()} to cart.")

    def calculate_total(self):
        """Menghitung total harga dari semua item di keranjang belanja."""
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
