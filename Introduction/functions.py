#what is function in python
#A function is a block of code that performs a specific task. It is reusable and can be called multiple times in a program. Functions help to break down complex problems into smaller, manageable pieces, making the code more organized and easier to read.   
#Functions can take input parameters, perform operations, and return output. They are defined using the 'def' keyword followed by the function name and parentheses. The code block within the function is indented. Functions can be called by their name followed by parentheses, and any required arguments can be passed within the parentheses.
#Functions are essential for code modularity and reusability, allowing developers to write cleaner and more efficient code. They can be built-in functions provided by Python or user-defined functions created by the programmer. Functions can also be used to implement various programming paradigms, such as procedural, object-oriented, and functional programming.
#In summary, functions in Python are fundamental building blocks that enable developers to create organized, reusable, and efficient code by encapsulating specific tasks into callable units.
#characteristics of functions in Python:
#1. Reusability: Functions can be defined once and called multiple times, allowing for code reuse and reducing redundancy.
#2. Modularity: Functions help break down complex problems into smaller, manageable pieces, making the code more organized and easier to read.
#3. Encapsulation: Functions encapsulate specific tasks, allowing for better organization and separation of concerns in the code.
#4. Parameters and Arguments: Functions can take input parameters, which are variables defined in the function definition, and arguments, which are the actual values passed to the function when it is called.
#5. Return Values: Functions can return values using the 'return' statement, allowing for the output of a function to be used in other parts of the code.
#6. Built-in and User-defined: Python provides a wide range of built-in functions for common tasks, and developers can also create their own user-defined functions to perform specific operations. 
#7. Variable Scope: Functions have their own local scope, meaning that variables defined within a function are not accessible outside of it, unless they are returned or declared as global.
#8. First-class Objects: In Python, functions are first-class objects, meaning they can be assigned to variables, passed as arguments to other functions, and returned from other functions, allowing for higher-order programming.
#Disadvantages of functions in Python:
#1. Overhead: Function calls can introduce overhead in terms of time and memory, especially if the function is called frequently or if it performs complex operations. This can lead to slower performance compared to inline code.
#2. Complexity: While functions can help break down complex problems, they can also add complexity to the codebase if not used properly. Overusing functions or creating too many small functions can make the code harder to read and understand.
#3. Debugging: Debugging functions can be more challenging than debugging inline code, especially if the function is called from multiple places in the code. It may require tracing through multiple function calls to identify the source of an issue.
#4. Scope Issues: Functions have their own local scope, which can lead to issues if variables are not properly managed. For example, if a variable is defined in a function and is not returned or declared as global, it cannot be accessed outside of the function, which can lead to errors if not handled correctly.
#5. Dependency: Functions can create dependencies between different parts of the code, especially if they rely on global variables or other functions. This can make the code less modular and harder to maintain if not managed properly.
#Overall, while functions are a powerful tool for organizing and structuring code, they should be used judiciously to avoid potential drawbacks and ensure that the code remains efficient, readable, and maintainable.

#Here are some examples of functions in Python:
#defining a function
def greet():
    #what we call comments in python functions
    #Docstring (Documentation String) is a special type of comment that is used to describe the purpose and behavior of a function. It is enclosed in triple quotes (""" """) and is typically placed immediately after the function definition. Docstrings provide a way to document the function's functionality, parameters, return values, and any other relevant information. They can be accessed using the built-in help() function or by using the __doc__ attribute of the function. Docstrings are an important part of writing clean and maintainable code, as they help other developers understand how to use the function and what it does without having to read through the implementation details.
    #In this example, the docstring provides a clear explanation of what the greet() function does, which is to print a greeting message to the console. It also mentions that the function does not take any parameters and does not return any value. This information can be helpful for other developers who may want to use or modify the function in the future, as it provides context and clarity about its purpose and behavior.
    #Comments, on the other hand, are used to provide additional explanations or notes about the code. They are ignored by the interpreter and do not affect the execution of the program. In this function, comments are used to explain what the function does and how it works, which can be helpful for other developers who may read the code in the future. Comments can also be used to temporarily disable code or to provide reminders for future improvements or changes.    #This is a simple function that prints a greeting message to the console. It does not take any parameters and does not return any value. The function can be called to execute the code within it, which in this case will display the greeting message.
    #Comments in Python are lines of text that are ignored by the interpreter and are used to provide explanations or notes about the code. In this function, the comments explain what the function does and how it works. Comments can be helpful for other developers who may read the code in the future, as they provide context and clarify the purpose of the function.
    #In this example, the comments are used to describe the function's purpose and its behavior. They help to make the code more understandable and maintainable by providing insights into what the function does and how it should be used.
    #Overall, comments are an essential part of writing clean and readable code, as they help to communicate the intent and functionality of the code to other developers who may work with it in the future.

    print("Hello, welcome to Python programming!")
#calling a function
greet()
#positional arguments
def greet(name, greeting):
    print(f"{greeting}, {name}! Welcome to Python programming!")
greet("Alice", "Hello")
#keyword arguments
def greet(name, greeting):
    print(f"{greeting}, {name}! Welcome to Python programming!")
greet(greeting="Hi", name="Bob")
#default arguments
def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}! Welcome to Python programming!")
greet()
greet("Charlie")
#returning values from a function
#A function can return a value using the 'return' statement. This allows the function to produce an output that can be used in other parts of the code. When a function is called, it executes its code and then returns the specified value to the caller. The returned value can be stored in a variable or used directly in expressions. Returning values from functions is essential for creating reusable and modular code, as it allows functions to perform specific tasks and provide results that can be utilized elsewhere in the program.
#In this example, the add() function takes two parameters, a and b, and returns their sum. When the function is called with the arguments 5 and 3, it calculates the sum and returns the result, which is then stored in the variable result. Finally, the result is printed to the console, displaying "The sum of 5 and 3 is: 8". This demonstrates how functions can return values that can be used in other parts of the code for further processing or output.
def add(a, b):
    return a + b
result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")
#recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
#lambda function (anonymous function)
square = lambda x: x * x
print(square(5))  # Output: 25
#higher-order function
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x * 2, 5)
print(result)  # Output: 10
#function with parameters
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming!")
greet("Alice")
#function with return value
def add(a, b):
    return a + b
result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")
#function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}! Welcome to Python programming!")
greet()
greet("Bob")
#function with variable number of arguments
def greet(*names):
    for name in names:
        print(f"Hello, {name}! Welcome to Python programming!")
greet("Alice", "Bob", "Charlie")
#function with keyword arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}! Welcome to Python programming!")
greet("Alice")
greet("Bob", greeting="Hi")

#global and local variables
#Global variables are variables that are defined outside of any function and can be accessed and modified from any part of the code, including inside functions. They have a global scope, meaning they are accessible throughout the entire program. Local variables, on the other hand, are variables that are defined within a function and can only be accessed and modified within that function. They have a local scope, meaning they are not accessible outside of the function in which they are defined. It is important to be cautious when using global variables, as they can lead to unintended consequences if modified from different parts of the code, while local variables help to encapsulate data and prevent conflicts between different parts of the program.
#Example of global and local variables     
global_var = "I am a global variable"
def my_function():
    local_var = "I am a local variable"
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable
my_function()
print(global_var)  # Accessing global variable
# The following line will raise an error because local_var is not accessible outside the function
# print(local_var)  # Uncommenting this line will cause an error


