# what is classes and objects
# class is a blueprint for creating objects. 
# It defines a set of attributes and methods that the objects created from the class will have. 
# An object is an instance of a class, which means it is a specific realization of the class with its own unique 
# set of attributes and behaviors.
# example of a class and an object
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"
# creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
# accessing the attributes of the object
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever

# calling the bark method on the object
print(my_dog.bark())  # Output: Woof!
