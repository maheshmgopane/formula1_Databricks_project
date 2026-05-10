#what is Dict?#Dict is a collection which is unordered, changeable and indexed. In Python, dictionaries are written
#with curly brackets, and they have keys and values.
#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and they have keys and values.
#characteristics of a dictionary:
#1. Unordered: The items in a dictionary are not ordered, meaning that they do not have a defined order. When you print a dictionary, the items may appear in a different order than they were defined.
#2. Changeable: You can change the values of a dictionary after it has been created. You can add new key-value pairs, modify existing ones, or remove them.
#3. Indexed: Each item in a dictionary has a key, which is used to access the corresponding value. The keys must be unique and immutable (e.g., strings, numbers, or tuples), while the values can be of any data type and can be duplicated.
#4. No duplicates: A dictionary cannot have duplicate keys. If you try to create a dictionary with duplicate keys, the last value assigned to that key will overwrite the previous value.
#5. Mutable: Dictionaries are mutable, meaning that you can change their content without changing their identity. You can add, remove, or modify key-value pairs in a dictionary.
#6. Dynamic: Dictionaries can grow and shrink as needed. You can add new key-value pairs or remove existing ones without having to define the size of the dictionary beforehand.
#7. Nesting: Dictionaries can contain other dictionaries, allowing for complex data structures. This is useful for representing hierarchical data or organizing related information.
#8. Iteration: You can iterate through the keys, values, or key-value pairs of a dictionary using loops. This allows you to perform operations on each item in the dictionary.
#9. Built-in methods: Python provides several built-in methods for working with dictionaries, such as keys(), values(), items(), get(), update(), and more. These methods make it easier to manipulate and access the data stored in a dictionary.
#10. Performance: Dictionaries in Python are implemented as hash tables, which provide fast access to values based on their keys. This makes dictionaries an efficient data structure for storing and retrieving data.
#11. Use cases: Dictionaries are commonly used for various applications, such as storing configuration settings, representing real-world objects (e.g., a person with attributes like name, age, and address), and implementing data structures like graphs and trees.
#In summary, dictionaries are a powerful and flexible data structure in Python that allows you to store and manipulate data in key-value pairs. They are widely used in programming for various applications due to their efficiency and ease of use.
#defination of a dictionary:    
#A dictionary is a collection which is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets, and they have keys and values.
#ways to create a dictionary:
#1. Using curly brackets {}:
dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(dict1)
#2. Using the dict() constructor:
dict2 = dict(name="John", age=36, country="Norway")
print(dict2)
#3. Using a list of tuples:
dict3 = dict([("brand", "Ford"), ("model", "Mustang"), ("year", 1964)])
print(dict3)
#4. Using keyword arguments:
dict4 = dict(brand="Ford", model="Mustang", year=1964)
print(dict4)
#5. Using a dictionary comprehension:
dict5 = {x: x**2 for x in (2, 3, 4)}
print(dict5)
#Accessing values in a dictionary:
#You can access the items of a dictionary by referring to its key name, inside square brackets:
x = dict1["model"]
print(x)
#You can also use the get() method to access the value of a key:    
y = dict1.get("model")
print(y)
#Modifying values in a dictionary:
#You can change the value of a specific item by referring to its key name:
dict1["year"] = 2020
print(dict1)
#You can also use the update() method to modify multiple items at once:
dict1.update({"year": 2020, "color": "red"})
print(dict1)
#Adding items to a dictionary:
#You can add a new item to a dictionary by using a new key and assigning a value to it:
dict1["color"] = "red"
print(dict1)
#You can also use the update() method to add multiple items at once:
dict1.update({"color": "red", "price": 20000})
print(dict1)
#Removing items from a dictionary:
#You can remove an item from a dictionary by using the pop() method, which removes the item with the specified key and returns its value:
removed_value = dict1.pop("color")
print(removed_value)
print(dict1)
#You can also use the del keyword to remove an item by its key:
del dict1["price"]
print(dict1)
#You can use the clear() method to remove all items from a dictionary:
dict1.clear()
print(dict1)
#You can use the del keyword to delete the entire dictionary:
del dict1
# print(dict1) # This will raise an error because dict1 has been deleted.

#methods of a dictionary:
#1. keys(): Returns a view object that displays a list of all the keys in the dictionary.
print(dict2.keys())
#2. values(): Returns a view object that displays a list of all the values in the dictionary.
print(dict2.values())   
#3. items(): Returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.
print(dict2.items())    
#4. get(): Returns the value of the specified key. If the key does not exist, it returns None (or a specified default value).
print(dict2.get("name"))
#5. update(): Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
dict2.update({"age": 30, "city": "Oslo"})
print(dict2)
#6. pop(): Removes the item with the specified key and returns its value. If the key does not exist, it raises a KeyError (or returns a specified default value).
removed_value = dict2.pop("age")
print(removed_value)
print(dict2)   
print(dict2.get("age", "Key not found")) # This will return "Key not found" because the key "age" has been removed from the dictionary.
#popitem(): Removes and returns an arbitrary key-value pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.
removed_item = dict2.popitem()  
print(removed_item)
print(dict2)
#7. clear(): Removes all items from the dictionary, leaving it empty.
dict2.clear()
print(dict2)
#8. copy(): Returns a shallow copy of the dictionary.
dict3_copy = dict3.copy()
print(dict3_copy)
#9. fromkeys(): Creates a new dictionary with the specified keys and a default value.
keys = ["a", "b", "c"]
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
#10. setdefault(): Returns the value of the specified key. If the key does not exist, it inserts the key with a specified default value and returns that value.
value = dict3.setdefault("color", "red")
print(value)
print(dict3)

#dist ionary comprehension:
#Dictionary comprehension is a concise way to create dictionaries. It consists of an expression pair (key: value) followed by a for statement inside curly braces {}. The expression can be any valid Python expression, and the for statement can be followed by an optional if statement to filter items.
#Example of dictionary comprehension:
squares = {x: x**2 for x in range(5)}
print(squares)
#This will create a dictionary where the keys are the numbers from 0 to 4, and the values are their squares. The output will be: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}.
#nested dictionary comprehension:
#You can also create nested dictionaries using dictionary comprehension. For example, if you want to create a dictionary of dictionaries that represents a multiplication table, you can do it like this:
multiplication_table = {i: {j: i * j for j in range(1, 11)} for i in range(1, 11)}
print(multiplication_table)
#This will create a dictionary where the keys are the numbers from 1 to 10, and the values are dictionaries that represent the multiplication results for each number. The output will be a nested dictionary with the multiplication table from 1 to 10.
#nested dictionary comprehension with filtering:
#You can also add a filter to the nested dictionary comprehension. For example, if you want to create a dictionary of dictionaries that represents a multiplication table but only includes the results that are even, you can do it like this:
even_multiplication_table = {i: {j: i * j for j in range(1, 11) if (i * j) % 2 == 0} for i in range(1, 11)}
print(even_multiplication_table)
#This will create a dictionary where the keys are the numbers from 1 to 10, and the values are dictionaries that represent the multiplication results for each number, but only include the even results. The output will be a nested dictionary with the even multiplication table from 1 to 10.
 #nested dictionary comprehension with string manipulation:
#You can also use string manipulation in the nested dictionary comprehension. For example, if you want
#to create a dictionary of dictionaries that represents the multiplication table but with the keys as strings, you can do it like this:
string_multiplication_table = {f"{i}": {f"{j}": f"{i} x {j} = {i * j}" for j in range(1, 11)} for i in range(1, 11)}
print(string_multiplication_table)
#This will create a dictionary where the keys are the numbers from 1 to 10 as strings, and the values are dictionaries that represent the multiplication results for each number, with the keys as strings and the values as formatted strings. The output will be a nested dictionary with the multiplication table from 1 to 10, with string keys and formatted string values.

#loops with dictionaries:
#You can use loops to iterate through the keys, values, or key-value pairs of a dictionary. For example, if you want to print all the keys in a dictionary, you can do it like this:
for key in dict3.keys():
    print(key)
#This will print all the keys in the dictionary dict3. You can also iterate through the values or key-value pairs using the values() and items() methods, respectively. For example, to print all the values in the dictionary, you can do it like this:
for value in dict3.values():
    print(value)
#To print all the key-value pairs in the dictionary, you can do it like this:
for key, value in dict3.items():
    print(f"{key}: {value}")
#This will print all the key-value pairs in the dictionary dict3 in the format "key: value". You can also use loops to perform operations on the items in the dictionary, such as modifying values or creating new dictionaries based on existing ones.
