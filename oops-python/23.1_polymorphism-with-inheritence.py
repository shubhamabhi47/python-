# ============================================================
# POLYMORPHISM THROUGH INHERITANCE
# ============================================================
# Runtime polymorphism occurs when multiple child classes inherit
# from a common parent and provide their own implementation of
# the same method.
#
# The caller can work with the common parent interface without
# needing to know the exact child class.
#
# Vehicle
#   ├── Car
#   └── Truck
#
# Both Car and Truck provide max_speed() and gear(), but their
# implementations are different.
# ============================================================


# ============================================================
# 1. BASE CLASS
# ============================================================
# The parent contains common state and common behavior.

class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Price: ₹{self.price}")


# ============================================================
# 2. CHILD CLASSES
# ============================================================
# Child classes inherit the common functionality from Vehicle
# and add/override their own behavior.

class Car(Vehicle):
    def max_speed(self):
        print("Car maximum speed: 100 km/h")

    def gear(self):
        print("Car has 6 gears")


class Truck(Vehicle):
    def max_speed(self):
        print("Truck maximum speed: 80 km/h")

    def gear(self):
        print("Truck has 7 gears")


car = Car("Swift", "Silver", 600000)
truck = Truck("Tata", "Red", 1200000)

car.get_details()
truck.get_details()


# ============================================================
# 3. RUNTIME POLYMORPHISM
# ============================================================
# Same method call:
#
#     vehicle.max_speed()
#
# Different actual objects:
#
#     Car   -> Car.max_speed()
#     Truck -> Truck.max_speed()
#
# Python determines the implementation at runtime.

vehicles = [car, truck]

for vehicle in vehicles:
    vehicle.max_speed()
    vehicle.gear()


# ============================================================
# 4. COMMON BASE-CLASS INTERFACE
# ============================================================
# The function does not need to know whether it receives a Car
# or Truck. It only depends on the Vehicle interface.

def display_vehicle(vehicle):
    vehicle.get_details()
    vehicle.max_speed()
    vehicle.gear()


display_vehicle(car)
display_vehicle(truck)


# ============================================================
# 5. METHOD OVERRIDING + super()
# ============================================================
# A child can completely replace a parent method or extend it
# using super().

class Vehicle:
    def start(self):
        print("Vehicle starting...")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine started")


class Truck(Vehicle):
    def start(self):
        super().start()
        print("Truck engine started")


for vehicle in [Car(), Truck()]:
    vehicle.start()


# ============================================================
# 6. POLYMORPHISM WITH A COMMON COLLECTION
# ============================================================
# A list can contain different subclasses as long as they provide
# the required interface.

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Truck(Vehicle):
    def move(self):
        print("Truck is carrying goods")


class Bike(Vehicle):
    def move(self):
        print("Bike is riding")


vehicles = [Car(), Truck(), Bike()]

for vehicle in vehicles:
    vehicle.move()


# ============================================================
# 7. PARENT REFERENCE TO CHILD OBJECT
# ============================================================
# Python variables are dynamically typed.
#
# A variable conceptually treated as a Vehicle can reference a
# Car or Truck object.
#
# The actual object's implementation is used at runtime.

vehicle: Vehicle = Car()
vehicle.move()

vehicle = Truck()
vehicle.move()


# ============================================================
# 8. isinstance() WITH POLYMORPHISM
# ============================================================
# Both objects are instances of Vehicle because Car and Truck
# inherit from Vehicle.

car = Car()
truck = Truck()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))

print(isinstance(truck, Truck))
print(isinstance(truck, Vehicle))


# ============================================================
# 9. ABSTRACT BASE CLASS + POLYMORPHISM
# ============================================================
# When every child MUST provide a particular method, an abstract
# base class can define the contract.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def gear(self):
        pass


class Car(Vehicle):
    def max_speed(self):
        return 100

    def gear(self):
        return 6


class Truck(Vehicle):
    def max_speed(self):
        return 80

    def gear(self):
        return 7


vehicles = [Car(), Truck()]

for vehicle in vehicles:
    print(f"Speed: {vehicle.max_speed()} km/h")
    print(f"Gears: {vehicle.gear()}")


# ============================================================
# 10. ADVANCED: ADDING A NEW CLASS
# ============================================================
# This demonstrates the main advantage of polymorphism.
#
# display_vehicle() does not need to change when a new Vehicle
# subclass is added, provided the subclass follows the same
# interface.

class Bus(Vehicle):
    def max_speed(self):
        return 90

    def gear(self):
        return 5


vehicles = [Car(), Truck(), Bus()]

for vehicle in vehicles:
    print(vehicle.max_speed(), vehicle.gear())


# ============================================================
# 11. POLYMORPHISM VS METHOD OVERLOADING
# ============================================================
# Method overriding:
#     Parent and child have the same method name.
#     Child changes the implementation.
#
# Method overloading:
#     Multiple methods with the same name but different parameter
#     lists.
#
# Python does not support traditional method overloading.
# Runtime polymorphism through overriding is natural in Python.


# ============================================================
# 12. ADVANCED DESIGN: POLYMORPHIC PROCESSING
# ============================================================
# The processing function depends only on the interface.
#
# This follows the Open/Closed Principle:
# existing processing code remains closed for modification while
# new vehicle types can be added through extension.

def process_vehicles(vehicles):
    for vehicle in vehicles:
        print(
            f"{vehicle.__class__.__name__}: "
            f"{vehicle.max_speed()} km/h, "
            f"{vehicle.gear()} gears"
        )


process_vehicles([
    Car(),
    Truck(),
    Bus()
])


# ============================================================
# KEY IDEA
# ============================================================
# INHERITANCE:
#     Car and Truck reuse Vehicle's common functionality.
#
# METHOD OVERRIDING:
#     Child classes provide specialized implementations.
#
# POLYMORPHISM:
#     The same call:
#
#         vehicle.max_speed()
#
#     can execute:
#
#         Car.max_speed()
#         Truck.max_speed()
#         Bus.max_speed()
#
# depending on the actual object.
#
# The important design principle is:
#
#     PROGRAM AGAINST AN INTERFACE,
#     NOT AGAINST A CONCRETE CLASS.
#
# This allows new subclasses to be added without rewriting the
# code that operates on the common interface.
# ============================================================