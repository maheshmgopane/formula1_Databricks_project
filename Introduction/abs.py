# What is abstraction in Python?
'''
Abstraction in Python means hiding internal implementation details and showing only the essential features of an object.

It helps reduce complexity and allows users to interact with objects without knowing how everything works internally.

Real-Life Example

Think about a car:

You use the steering, brake, and accelerator
You don’t need to know the internal engine mechanism to drive it

That is abstraction.

Abstraction in Python

Python supports abstraction using:

Abstract Classes
Abstract Methods

These are available through the built-in abc module.

Example'''
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

# Child class
class Car(Vehicle):

    def start(self):
        print("Car is starting...")

# Object creation
c = Car()
c.start()
'''Output
Car is starting...
Important Points
ABC → Abstract Base Class
@abstractmethod → Method that must be implemented in child classes
You cannot create an object of an abstract class directly

Example:

v = Vehicle()   # Error
Benefits of Abstraction
Hides unnecessary details
Improves security
Makes code easier to maintain
Reduces complexity
Encourages standard structure
Simple One-Line Definition

Abstraction is the process of hiding implementation details and showing only essential functionality to the user.

Types of Abstraction in Python

1. Abstract Classes and Methods: Using the abc module to define abstract base classes with methods that must be implemented by subclasses.

2. Encapsulation: Hiding internal data using private attributes (prefixed with _) and providing public methods to access them.

Examples

Example 1: Abstract Class (as above)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

c = Car()
c.start()  # Output: Car is starting...

Example 2: Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
