# what is constructor in python?
# A constructor in Python is a special method that is automatically called when an object of a class is created.
#  It is used to initialize the attributes of the class and set up any necessary resources for the object. 
# The constructor method is defined using the __init__() function.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
# In this example, the __init__() method is the constructor for the Person class.
# It takes two parameters, name and age, and initializes the corresponding attributes of the class.
# The constructor is called automatically when we create an object of the Person class, and it sets the name and age attributes for that object.
# Constructors can also have default values for parameters, allowing you to create objects without providing all the arguments.
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
# creating an object of the Person class without providing arguments
person2 = Person()
print(person2.name)  # Output: Unknown
print(person2.age)   # Output: 0
# In this example, the __init__() method has default values for the name and age parameters.
# When we create an object of the Person class without providing any arguments, the constructor uses the default values to initialize the attributes of the object.
# Constructors can also perform additional tasks, such as validating input or setting up connections to databases or other resources.
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = self.connect_to_database()
    
    def connect_to_database(self):
        # Code to establish a connection to the database
        return f"Connected to database at {self.host}:{self.port}"  
# creating an object of the DatabaseConnection class
db_connection = DatabaseConnection("localhost", 5432)
print(db_connection.connection)  # Output: Connected to database at localhost:5432
# In this example, the __init__() method initializes the host and port attributes and also calls the connect_to_database() method to establish a connection to the database.
# In summary, a constructor in Python is a special method that initializes the attributes of a class and sets up any necessary resources for an object when it is created. It is defined using the __init__() function and can have default values for parameters.
# Note: The __init__() method is not the only special method in Python; there are other special methods like __str__(), __repr__(), and __del__() that serve different purposes in a class. 
# However, the __init__() method is specifically used for object initialization and is commonly referred to as the constructor in Python.
# It's important to note that the __init__() method does not return any value; it is used solely for initializing the attributes of the class.
# If you need to perform any cleanup tasks when an object is destroyed, you can use the __del__() method, which is called when an object is garbage collected. However, it's generally recommended to avoid using __del__() for cleanup tasks and instead use context managers or other techniques for resource management.
# In conclusion, constructors are an essential part of object-oriented programming in Python, allowing you to initialize objects with specific attributes and set up necessary resources when they are created.
# By using constructors effectively, you can create more robust and maintainable code in your Python applications.
# It's also worth mentioning that Python does not support method overloading like some other programming languages, so you cannot have multiple __init__() methods with different parameters. However, you can achieve similar functionality by using default parameter values or by using *args and **kwargs to handle variable numbers of arguments in the constructor.
# Example of using *args and **kwargs in a constructor
class Person:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.additional_info = kwargs       
# creating an object of the Person class with additional information
person3 = Person("Bob", 25, city="New York", occupation="Engineer")
print(person3.name)  # Output: Bob
print(person3.age)   # Output: 25
print(person3.additional_info)  # Output: {'city': 'New York', 'occupation': 'Engineer'}
# In this example, the __init__() method takes additional arguments using *args and **kwargs. The *args allows for any number of positional arguments, while **kwargs allows for any number of keyword arguments. The additional information is stored in the additional_info attribute as a dictionary.
# In summary, constructors in Python are a powerful tool for initializing objects and setting up necessary resources. They allow you to create objects with specific attributes and can handle variable numbers of arguments using *args and **kwargs. By understanding how to use constructors effectively, you can write more efficient and maintainable code in your Python applications.
# Types of Constructors in Python:
# 1. Default Constructor: A constructor that takes no parameters and initializes the attributes with default values.
# Example of a default constructor
class Person:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0    
# creating an object of the Person class using the default constructor
person1 = Person()
print(person1.name)  # Output: Unknown
print(person1.age)   # Output: 0

# 2. Parameterized Constructor: A constructor that takes parameters to initialize the attributes of the class.
# Example of a parameterized constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# creating an object of the Person class using the parameterized constructor
person2 = Person("Alice", 30)
print(person2.name)  # Output: Alice
print(person2.age)   # Output: 30

# 3. Copy Constructor: A constructor that creates a new object as a copy of an existing object. Python does not have a built-in copy constructor, but you can achieve similar functionality using the copy module or by defining a method to create a copy of an object.
# Example of a copy constructor using the copy module
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# creating an object of the Person class
person3 = Person("Bob", 25)
# creating a copy of the person3 object using the copy module
person4 = copy.copy(person3)
print(person4.name)  # Output: Bob
print(person4.age)   # Output: 25
# In this example, we use the copy.copy() function to create a shallow copy of the person3 object. The person4 object is a new instance of the Person class with the same attributes as person3. Note that if the attributes of the class are mutable (like lists or dictionaries), a shallow copy will not create a new instance of those attributes, and changes to them will affect both the original and the copied object. In such cases, you may want to use copy.deepcopy() to create a deep copy of the object.     
# Example of a copy constructor using a method to create a copy of an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def copy(self):
        return Person(self.name, self.age)
# creating an object of the Person class
person5 = Person("Charlie", 40)
# creating a copy of the person5 object using the copy method
person6 = person5.copy()
print(person6.name)  # Output: Charlie
print(person6.age)   # Output: 40
# In this example, we define a copy() method within the Person class that creates and returns a new instance of the Person class with the same attributes as the original object. The person6 object is a new instance of the Person class with the same name and age as person5. This approach allows you to create a copy of an object without relying on the copy module, and it can be customized to handle any specific copying logic you may need for your class.
