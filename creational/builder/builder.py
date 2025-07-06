class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.wheels} wheels, color {self.color}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self, engine: str):
        self.car.engine = engine
        return self

    def wheels(self, wheels: int):
        self.car.wheels = wheels
        return self
    
    def color(self, color: str):
        self.car.color = color
        return self
    
    def build(self):
        return self.car


if __name__ == "__main__":
    builder = CarBuilder()
    sports_car = builder.add_engine("V8").wheels(4).color("Red").build()
    print(sports_car)