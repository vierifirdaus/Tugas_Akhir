class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):  # Inheritance
    def speak(self):
        print("Bark")

# Usage
dog = Dog()
dog.speak()  # Output: Bark