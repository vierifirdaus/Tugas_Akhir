class Person:
    def __init__(self, name):
        self.__name = name  # Encapsulation
    
    def get_name(self):
        return self.__name

class Student(Person):  # Inheritance
    def __init__(self, name, id):
        super().__init__(name)
        self.__id = id  # Encapsulation tambahan

# Usage
student = Student("Alice", "123")
print(student.get_name())  # Output: Alice (warisan method)