# What is Encapsulation in Python?
# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP) in Python. It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. Encapsulation also involves restricting access to certain components of an object, which is achieved through access modifiers.
# In Python, there are three types of access modifiers:
# 1. Public: Attributes and methods that are accessible from anywhere. They are defined without any special prefix.
# 2. Protected: Attributes and methods that are intended to be accessed only within the class and its subclasses. They are defined with a single underscore prefix (e.g., _protected_attribute).
# 3. Private: Attributes and methods that are intended to be accessed only within the class. They are defined with a double underscore prefix (e.g., __private_attribute). Private members cannot be accessed directly from outside the class, and Python uses name mangling to make them harder to access.
# Encapsulation helps to protect the internal state of an object and prevents unauthorized access or modification. It also promotes modularity and maintainability by allowing the internal implementation of a class to be changed without affecting the external code that uses the class.    
# Example of Encapsulation in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make  # Public attribute
        self.model = model  # Public attribute
        self.year = year  # Public attribute
        self._speed = 0  # Protected attribute
        self.__engine_status = "off"  # Private attribute

    def start_engine(self):
        self.__engine_status = "on"
        print("Engine started.")

    def stop_engine(self):
        self.__engine_status = "off"
        print("Engine stopped.")

    def accelerate(self):
        if self.__engine_status == "on":
            self._speed += 10
            print(f"Accelerating. Current speed: {self._speed} km/h")
        else:
            print("Cannot accelerate. Engine is off.")

    def decelerate(self):
        if self.__engine_status == "on" and self._speed > 0:
            self._speed -= 10
            print(f"Decelerating. Current speed: {self._speed} km/h")
        else:
            print("Cannot decelerate. Engine is off or speed is already zero.")
