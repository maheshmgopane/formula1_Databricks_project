#what is decorators in python?#Decorators in Python are a powerful and flexible way to modify the behavior of 
# functions or classes without changing their source code. They are often used to add functionality to existing 
# code in a clean and reusable manner. A decorator is essentially a function that takes another function as an 
# argument and returns a new function that can enhance or modify the behavior of the original function.
#Here's a simple example of a decorator that adds logging functionality to a function:
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
@log_decorator
def add(a, b):
    return a + b
# When you call the add function, it will now log the input arguments and the return value:
add(3, 5)
# Output:
# Calling function 'add' with arguments: (3, 5) and keyword arguments: {}
# Function 'add' returned: 8
#In this example, the log_decorator function takes the add function as an argument and returns a new function (wrapper) that adds logging before and after calling the original add function. The @log_decorator syntax is a shorthand for applying the decorator to the add function.
#Decorators can also be used with classes, and they can be stacked to apply multiple decorators
# to a single function. They are widely used in Python for various purposes, such as authentication, caching, and performance measurement.
