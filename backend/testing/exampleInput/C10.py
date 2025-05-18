from abc import ABC, abstractmethod

class Animal(ABC):
    def make_sound(self):
        pass

    def move(self):
        pass

# Concrete Class implementing both
class Bird(Animal):
    def make_sound(self):
        return "Chirp"

    def move(self):
        return "Hop"

    def fly(self):
        return "Flap wings and fly"
