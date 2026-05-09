# what is lambda function in python
# lambda function is a anonymous function which can have any number of arguments but only one expression.   
# syntax of lambda function is
# lambda arguments: expression
# example of lambda function
# add two numbers using lambda function
add = lambda x, y: x + y
print(add(2, 3))  # output: 5
# example of lambda function with filter function
# filter even numbers from a list using lambda function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # output: [2, 4, 6]
# example of lambda function with map function
# square of numbers in a list using lambda function
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # output: [1, 4, 9, 16, 25, 36]
# example of lambda function with reduce function
from functools import reduce
# product of numbers in a list using lambda function
product = reduce(lambda x, y: x * y, numbers)
print(product)  # output: 720
# example of lambda function with sorted function
# sort a list of tuples based on the second element using lambda function
tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # output: [(1, 'one'), (3, 'three'), (2, 'two')]
# example of lambda function with list comprehension
# filter odd numbers from a list using lambda function
odd_numbers = [x for x in numbers if (lambda x: x % 2 != 0)(x)]
print(odd_numbers)  # output: [1, 3, 5]
# example of lambda function with reduce function to find the maximum number in a list
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # output: 6
# example of lambda function with reduce function to find the minimum number in a list
min_number = reduce(lambda x, y: x if x < y else y, numbers)
print(min_number)  # output: 1
# example of lambda function with reduce function to find the sum of numbers in a list
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # output: 21
# example of lambda function with reduce function to find the average of numbers in a list
average = reduce(lambda x, y: x + y, numbers) / len(numbers)
print(average)  # output: 3.5
# example of lambda function with reduce function to find the factorial of a number
factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial)  # output: 120
