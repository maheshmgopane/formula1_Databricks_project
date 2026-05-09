# What is OOPS?# 
# OOPS stands for Object-Oriented Programming System. It is a programming paradigm that uses objects and classes to design and structure software. OOPS allows developers to create modular, reusable, and maintainable code by organizing data and behavior into objects. The main principles of OOPS include:
#1. Encapsulation: This principle involves bundling data and methods that operate on that data within a single unit called a class. It helps to hide the internal details of an object and only expose necessary information through public methods.
#2. Inheritance: This principle allows a new class (called a subclass or child class) to inherit properties and behaviors from an existing class (called a superclass or parent class). This promotes code reusability and establishes a natural hierarchical relationship between classes.
#3. Polymorphism: This principle allows objects of different classes to be treated as objects of    a common superclass. It enables a single interface to represent different underlying forms (data types). Polymorphism can be achieved through method overriding and method overloading.
#4. Abstraction: This principle involves hiding the complex implementation details of a system and exposing only the necessary features to the user. It allows developers to focus on what an object does rather than how it does it, making it easier to manage and understand complex systems.    
# OOPS is widely used in programming languages such as Java, C++, Python, and many others. It helps developers to create more efficient and organized code, making it easier to maintain and extend software applications.  
## Example of OOPS in Python:
class Animal: # This is a base class (superclass)
    def __init__(self, name):# This is the constructor method that initializes the name attribute of the Animal class.
        self.name = name#

    def speak(self): # This is a method that will be overridden by subclasses to provide specific behavior for different types of animals.`
        pass #
class Dog(Animal): # This is a derived class (subclass) that inherits from the Animal class.
    def speak(self): # This method overrides the speak method of the Animal class to provide specific behavior for dogs.
        return f"{self.name} says Woof!" # This returns a string that includes the name of the dog and the sound it makes.
class Cat(Animal): # This is another derived class (subclass) that inherits from the Animal class.
    def speak(self): # This method overrides the speak method of the Animal class to provide specific behavior for cats.
        return f"{self.name} says Meow!" # This returns a string that includes the name of the cat and the sound it makes.  
# Creating instances of the Dog and Cat classes
dog = Dog("Buddy") # This creates an instance of the Dog class with the name "Buddy".
cat = Cat("Whiskers") # This creates an instance of the Cat class with the name "Whiskers".
# Calling the speak method on both instances
print(dog.speak()) # This will print "Buddy says Woof!"
print(cat.speak()) # This will print "Whiskers says Meow!"  