class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary
    
    # Getter/Setter untuk encapsulation
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

# Usage
emp = Employee("John", 5000)
print(emp.get_salary())  # Output: 5000