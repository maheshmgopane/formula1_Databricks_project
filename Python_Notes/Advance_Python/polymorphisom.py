"""Polymorphism examples in Python.

Polymorphism means "many forms." In object-oriented programming,
objects of different classes can be accessed through the same interface.
"""

class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"


def animal_sound(animal):
    """Demonstrates polymorphism by calling the same method on different objects."""
    print(animal.speak())


# Duck typing example: no shared base class required
class Car:
    def start(self):
        return "Car engine starting"

class Airplane:
    def start(self):
        return "Airplane engines starting"


def start_vehicle(vehicle):
    """Duck typing: object only needs a start() method."""
    print(vehicle.start())


if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow()]
    for animal in animals:
        animal_sound(animal)

    vehicles = [Car(), Airplane()]
    for vehicle in vehicles:
        start_vehicle(vehicle)
