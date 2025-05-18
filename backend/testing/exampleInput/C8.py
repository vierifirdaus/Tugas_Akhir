class Person:
    def __init__(self, name, age):
        self._name = name  # Atribut privat
        self._age = age    # Atribut privat

    # Getter untuk name
    def name(self):
        return self._name

    # Setter untuk name
    def name(self, new_name):
        self._name = new_name

    # Getter untuk age
    def age(self):
        return self._age

    # Setter untuk age
    def age(self, new_age):
        self._age = new_age