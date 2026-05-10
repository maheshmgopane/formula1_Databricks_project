# What is generator?
# A generator is a special type of function that returns an iterator. It allows you to iterate
# through a sequence of values without having to store the entire sequence in memory at once.
# A generator is defined using a function with the 'yield' keyword. When the function is called,
# it returns a generator object that can be iterated over. Each time the 'yield' statement is
# executed, the generator produces a value and pauses its execution, resuming from the same point
# when the next value is requested.
# Example of a generator function that generates the Fibonacci sequence:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a # Yield the current Fibonacci number, then pause execution
        a, b = b, a + b
# Using the generator to get the first 10 Fibonacci numbers
for num in fibonacci(10):
    print(num)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# In this example, the 'fibonacci' function is a generator that yields Fibonacci numbers up to 'n'. When we iterate over the generator, it produces each Fibonacci number one at a time, allowing us to efficiently generate the sequence without storing all values in memory.
# Generators are particularly useful when working with large datasets or infinite sequences, as they allow you to process data on-the-fly without consuming excessive memory.   
# Generators can also be created using generator expressions, which are similar to list comprehensions but use parentheses instead of square brackets. For example:
squares = (x**2 for x in range(10))
for square in squares:
    print(square)
# Output:
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# In this example, the generator expression creates a generator that produces the squares of numbers from 0 to 9. When we iterate over the generator, it yields each square one at a time.
# In summary, generators are a powerful tool in Python for creating iterators that can produce values on-the-fly, allowing for efficient memory usage and the ability to work with large or infinite sequences of data.

