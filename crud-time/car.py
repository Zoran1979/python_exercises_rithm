class Car():

    id = 1

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.id = Car.id
        Car.id += 1
