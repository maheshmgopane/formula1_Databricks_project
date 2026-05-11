'''
Default argument: a parameter given a default value in the function definition.
Keyword argument: an argument passed to a function by explicitly naming the parameter.
Arguments vs keyword arguments:
    - Positional arguments are passed by order.
    - Keyword arguments are passed by name.
'''

def greet(name="Guest", message="Hello"):
    print(f"{message}, {name}!")

# Default arguments are used when values are not provided.
greet()

# Positional arguments are passed in order.
greet("Alice", "Hi")

# Keyword arguments are passed by parameter name.
greet(message="Welcome", name="Bob")

# Mixed usage: positional first, keyword after.
greet("Charlie", message="Good morning")


def example(a, b=10, c=20):
    return a + b + c

# Positional argument only, uses default b and c.
result1 = example(1)

# Keyword arguments specify parameters by name.
result2 = example(a=1, c=5)

# Mixed usage with a positional argument and a keyword argument.
result3 = example(1, c=5)

print(result1, result2, result3)

