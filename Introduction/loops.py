#loops in python
#for loop
# A for loop is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in the sequence. The syntax of a for loop is:
# for variable in sequence: 
#     # code to execute for each item in the sequence
# Example of a for loop to print numbers from 1 to 5
for i in range(1, 6):# The range function generates numbers from 1 to 5 (6 is exclusive)
    print(i) # Print the current value of i
#while loop
# A while loop is used to execute a block of code as long as a specified condition is true. The syntax of a while loop is:
# while condition:
#     # code to execute as long as the condition is true
# Example of a while loop to print numbers from 1 to 5
i = 1# Initialize the variable i to 1
while i <= 5:# Continue the loop as long as i is less than or equal to 5
    print(i)# Print the current value of i
    i += 1# Increment i by 1 to move to the next number
#loops are useful for performing repetitive tasks without having to write the same code multiple times. They can be used to iterate over data structures, perform calculations, and automate tasks.
# In Python, you can also use nested loops (a loop inside another loop) to perform more complex iterations. Additionally, you can use control flow statements like break and continue to manage the flow of your loops.
# It's important to ensure that your loops have a terminating condition to avoid infinite loops, which can cause your program to crash or become unresponsive.
# Example of a nested loop to print a multiplication table
for i in range(1, 6):# Outer loop to iterate through numbers 1 to 5
    for j in range(1, 6):# Inner loop to iterate through numbers 1 to 5
        print(f"{i} x {j} = {i * j}")# Print the multiplication result in a formatted string
    print()# Print a blank line after each row of the multiplication table  
# Example of using break to exit a loop
for i in range(1, 10):# Loop through numbers from 1 to 9
    if i == 5:# If i is equal to 5, break out of the loop
        break# Print the current value of i (this will print numbers from 1 to 4)
    print(i)
# Example of using continue to skip an iteration
for i in range(1, 10):# Loop through numbers from 1 to 9
    if i % 2 == 0:# If i is even, skip the rest of the loop and continue with the next iteration
        continue# Print the current value of i (this will print only odd numbers from 1 to 9)
    print(i)
# Example of using pass to do nothing
for i in range(1, 10):# Loop through numbers from 1 to 9
    if i == 5:# If i is equal to 5, do nothing
        pass# Print the current value of i (this will print all numbers from 1 to 9)
    print(i)    
# In summary, loops are a fundamental part of programming that allow you to execute a block of code multiple times based on a condition or over a sequence. They help you automate repetitive tasks and manage the flow of your program efficiently.
# It's important to use loops wisely and ensure that they have a clear terminating condition to avoid infinite loops. Additionally, using control flow statements like break and continue can help you manage the flow of your loops effectively.
# Practice using loops in your programming projects to become more comfortable with their syntax and functionality. You can experiment with different types of loops and control flow statements to see how they work in various scenarios.
# Happy coding!
#loops with lambda functions
# Lambda functions are anonymous functions that can be defined in a single line of code. They are often used in conjunction with loops to perform operations on each item in a sequence. The syntax of a lambda function is:
# lambda arguments: expression
# Example of using a lambda function with a for loop to square numbers in a list
numbers = [1, 2, 3, 4, 5]# A list of numbers to be squared
squared_numbers = []# An empty list to store the squared numbers        
for num in numbers:# Loop through each number in the list
    squared = (lambda x: x ** 2)(num)# Use a lambda function to square the number
    squared_numbers.append(squared)# Append the squared number to the squared_numbers list
print(squared_numbers)# Print the list of squared numbers
# Example of using a lambda function with a while loop to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]# A list of numbers to be filtered
even_numbers = []# An empty list to store the even numbers
i = 0# Initialize the variable i to 0
while i < len(numbers):# Continue the loop as long as i is less than the length
    num = numbers[i]# Get the current number from the list
    if (lambda x: x % 2 == 0)(num):# Use a lambda function to check if the number is even
        even_numbers.append(num)# If the number is even, append it to the even_numbers list
    i += 1# Increment i by 1 to move to the next number
print(even_numbers)# Print the list of even numbers
# In summary, lambda functions can be a powerful tool when used in conjunction with loops to perform operations on each item in a sequence. They allow you to write concise and efficient code for simple operations without the need for defining a separate function. However, it's important to use lambda functions judiciously and ensure that they enhance the readability of your code rather than making it more complex.
# Practice using lambda functions with loops in your programming projects to become more comfortable with their syntax and functionality. You can experiment with different types of operations and sequences to see how lambda functions can simplify your code.


