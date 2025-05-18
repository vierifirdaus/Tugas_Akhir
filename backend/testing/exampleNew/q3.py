class Bird:
    def fly(self):
        print("Flying high")

class Penguin(Bird):
    def fly(self):  # Method overriding
        print("Cannot fly")

# Usage
birds = [Bird(), Penguin()]
for bird in birds:
    bird.fly()  # Output: Flying high / Cannot fly