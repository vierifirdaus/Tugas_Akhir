class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started with {} horsepower".format(self.horsepower)

    def stop(self):
        return "Engine stopped"

class Car:
    def __init__(self, horsepower):
        self.engine = Engine(horsepower)  # Car bergantung pada Engine

    def start_car(self):
        return f"{self.engine.start()}"

    def stop_car(self):
        return f"{self.engine.stop()}"

def main():
    my_car = Car(150)  # Membuat objek Car dengan 150 tenaga kuda
    print(my_car.start_car())  # Memulai mobil
    print(my_car.stop_car())   # Menghentikan mobil

def funca(a):
    return f"Function {a} "

main()
a=5
funca(a)
a=10
funca(a)
