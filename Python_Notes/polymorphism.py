# what is polymorphism?
# polymorphism is the ability of an object to take on many forms.   
# in python, polymorphism is achieved through method overriding.
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"  
class Cat(Animal):
    def speak(self):
        return "Cat meows"
# we can create a list of animals and call the speak method on each animal
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# output:
# Dog barks
# Cat meows
# we can also create a function that takes an animal as an argument and calls the speak method
def make_animal_speak(animal):
    print(animal.speak())   
make_animal_speak(Dog())  # output: Dog barks
make_animal_speak(Cat())  # output: Cat meows
# in this example, the make_animal_speak function can take any animal object and call the speak method, demonstrating polymorphism.
#polymorphism allows us to write code that is more flexible and reusable, as we can use the same function to work with different types of objects.
# in python, we can also achieve polymorphism through duck typing, which is a concept that states that if an object behaves like a certain type, it can be treated as that type.
class Bird:
    def speak(self):
        return "Bird chirps"

# we can now call the make_animal_speak function with a Bird object
make_animal_speak(Bird())  # output: Bird chirps    
# even though the Bird class does not inherit from the Animal class, it can still be treated as an animal because it has a speak method. This is an example of duck typing in python.
# in summary, polymorphism is a powerful concept in object-oriented programming that allows us to write code that can work with different types of objects in a flexible and reusable way.
# it is achieved through method overriding and duck typing in python.
# polymorphism is a fundamental concept in object-oriented programming that allows us to write code that can work with different types of objects in a flexible and reusable way.
# it is achieved through method overriding and duck typing in python.
# in python, we can also achieve polymorphism through operator overloading, which allows us to define how operators work with our custom classes.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = point1 + point2
print(point3)  # output: Point(4, 6)
# in this example, we have defined the __add__ method to allow us to add two Point objects together using the + operator. This is an example of operator overloading, which is another way to achieve polymorphism in python.
# in summary, polymorphism is a powerful concept in object-oriented programming that allows us to write code that can work with different types of objects in a flexible and reusable way. It is achieved through method overriding, duck typing, and operator overloading in python.   
