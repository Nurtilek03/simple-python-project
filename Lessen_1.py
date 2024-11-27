class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def calculate_travel_time(self, distance):
        return 0

    def display_info(self):
        print(f"Транспортное средство: {self.name}, Максимальная скорость: {self.max_speed} км/ч")

class Car(Vehicle):
    def calculate_travel_time(self, distance):
        return distance / self.max_speed

class Bicycle(Vehicle):
    def calculate_travel_time(self, distance):
        base_time = distance / self.max_speed
        return base_time * 1.2

class Plane(Vehicle):
    def calculate_travel_time(self, distance):
        base_time = distance / self.max_speed
        return base_time + 1  

def calculate_and_display_travel(vehicle, distance):
    vehicle.display_info()
    travel_time = vehicle.calculate_travel_time(distance)
    print(f"Время на преодоление расстояния {distance} км: {travel_time:.2f} часов\n")

car = Car("Автомобиль", 120)
bicycle = Bicycle("Велосипед", 20)
plane = Plane("Самолет", 800)

distance = 500

calculate_and_display_travel(car, distance)
calculate_and_display_travel(bicycle, distance)
calculate_and_display_travel(plane, distance)
