class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def drive(self):
        print("Driving")

class ElectricCar(Car):  # Multi-level
    def charge(self):
        print("Charging")

# Usage
tesla = ElectricCar()
tesla.move()  # Output: Moving (dari grandparent)