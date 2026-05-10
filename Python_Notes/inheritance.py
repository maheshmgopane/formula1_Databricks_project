# What is inheritance in Python?
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
# Types: Single, Multiple, Multilevel, Hierarchical, Hybrid.
# Use: Code reuse, polymorphism, method overriding.

# Example: Single Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Example: Multiple Inheritance
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

# Example: Multilevel Inheritance
class Grandparent:
    def grand_method(self):
        return "Grandparent method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent method"

class Child(Parent):
    def child_method(self):
        return "Child method"

# Example: Hierarchical Inheritance
class Vehicle:
    def drive(self):
        return "Driving"

class Car(Vehicle):
    def car_feature(self):
        return "Car feature"

class Bike(Vehicle):
    def bike_feature(self):
        return "Bike feature"

# Example: Hybrid Inheritance (combination of multiple and multilevel)
class X:
    def x_method(self):
        return "X method"

class Y(X):
    def y_method(self):
        return "Y method"

class Z(X):
    def z_method(self):
        return "Z method"

class W(Y, Z):
    def w_method(self):
        return "W method" 