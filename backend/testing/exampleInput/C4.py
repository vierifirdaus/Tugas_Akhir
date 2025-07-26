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
