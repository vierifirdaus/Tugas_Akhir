from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):  # Implementasi abstract method
        return 3.14 * self.radius ** 2

# Usage
circle = Circle()
circle.radius = 5
print(circle.area())  # Output: 78.5