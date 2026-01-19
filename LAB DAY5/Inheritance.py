
class Vehicle:
    vehicle_count = 0   # class variable

    def __init__(self, name):
        self.name = name
        Vehicle.vehicle_count += 1

    def start(self):
        print(f"{self.name} vehicle started")

    @classmethod
    def total_vehicles(cls):
        print("Total vehicles created:", cls.vehicle_count)


# Single Inheritance
class Car(Vehicle):
    def drive(self):
        print(f"{self.name} car is driving")


# Multilevel Inheritance
class ElectricCar(Car):
    def charge(self):
        print(f"{self.name} electric car is charging")

v1 = Vehicle("Generic")
v1.start()

c1 = Car("BMW")
c1.start()
c1.drive()

e1 = ElectricCar("Tesla")
e1.start()
e1.drive()
e1.charge()

Vehicle.total_vehicles()
