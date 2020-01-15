class Airplane():
    def __init__(self, mark, model, year, max_speed):
        self.mark = mark
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0 
        self.is_flying = False

    def take_off(self):
        self.is_flying = True

    def land(self):
        self.is_flying = False

    def fly(self):
        self.odometer += 10

    def result(self):
        return f"{self.mark} {self.model} made in {self.year}, {self.is_flying} odometer: {self.odometer}, max speed is {self.max_speed} km/h"

plane = Airplane("Airbus", "A380", "2015", "1.185")
print(plane.result())
plane.take_off()
print(plane.result())