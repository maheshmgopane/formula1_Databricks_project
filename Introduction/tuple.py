#what is tuple in python#tuple is a collection of ordered and immutable elements. It is defined using parentheses () and can contain elements of different data types. Once a tuple is created, its elements cannot be modified, added, or removed. Tuples are often used to group related data together and can be accessed using indexing and slicing.
#Here are some key features of tuples in Python:
#1. Ordered: The elements in a tuple maintain the order in which they were defined.
#2. Immutable: Once a tuple is created, its elements cannot be changed. You cannot add, remove, or modify elements in a tuple.
#3. Heterogeneous: A tuple can contain elements of different data types, such as integers, strings, floats, and booleans.
#4. Indexing and Slicing: You can access individual elements of a tuple using indexing (starting from 0) and slicing to retrieve a range of elements.
#5. Tuple Packing and Unpacking: You can create a tuple by packing values together, and you can also unpack a tuple into individual variables.
#Example of creating a tuple
my_tuple = (1, "Hello", 3.14, True)
#way to create a tuple without parentheses
my_tuple = 1, "Hello", 3.14, True
#Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: Hello
print(my_tuple[2])  # Output: 3.14
print(my_tuple[3])  # Output: True
#Slicing a tuple
print(my_tuple[1:3])  # Output: ('Hello', 3.14)
#Tuple packing and unpacking
a, b, c, d = my_tuple
print(a)  # Output: 1
print(b)  # Output: Hello
print(c)  # Output: 3.14
print(d)  # Output: True
#Tuples are commonly used in situations where you want to group related data together and ensure that it remains unchanged throughout the program. They can also be used as keys in dictionaries or as elements in sets, as they are hashable due to their immutability.    
