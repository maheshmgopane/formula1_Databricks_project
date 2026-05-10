# What are errors? Types of errors

"""In Python, an error is a problem in the program that causes it to stop or behave unexpectedly.

Types of Errors in Python:
- Syntax Errors
- Runtime Errors (Exceptions)
- Logical Errors

1. Syntax Error
Occurs when Python rules (syntax) are written incorrectly.

Example:
print("Hello"
# Output: SyntaxError: '(' was never closed

2. Runtime Error (Exception)
Occurs while the program is running.

Example:
a = 10 / 0
# Output: ZeroDivisionError: division by zero

3. Logical Error
Program runs successfully but gives wrong output because the logic is incorrect.

Example:
a = 10
b = 20
print(a - b)
# Output: -10
# Expected output should be 30.

Summary Table:
Error Type	Occurs When	Example
Syntax Error	Wrong syntax	Missing :
Runtime Error	During execution	Divide by zero
Logical Error	Wrong logic	Incorrect formula

Simple One-Line Definition:
Errors are problems in a program that cause incorrect execution, abnormal termination, or wrong output.
"""

# What is error handling in Python?
# Error handling in Python is the process of managing runtime errors so the program does not crash unexpectedly.

# Python uses try, except, else, and finally to handle errors.

# Basic Syntax:
try:
    # code that may cause error
    pass
except Exception as e:
    # code to handle error
    pass
else:
    # runs if no exception occurs
    pass
finally:
    # runs whether or not an error occurs
    pass

# Example: simple exception handling
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Example: multiple exception handling
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Result:", result)
finally:
    print("End of example")

# Nested try blocks
try:
    value = input("Enter a number: ")
    try:
        num = int(value)
    except ValueError:
        print("ValueError: Please enter a valid integer")
    else:
        try:
            result = 10 / num
        except ZeroDivisionError:
            print("ZeroDivisionError: Cannot divide by zero")
        else:
            print("Result:", result)
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Nested try blocks example completed")

# Common Python Exceptions:
# ZeroDivisionError: Division by zero
# ValueError: Invalid value
# TypeError: Wrong data type
# IndexError: Invalid list index
# KeyError: Invalid dictionary key
# FileNotFoundError: File does not exist

# Simple One-Line Definition:
# Error handling in Python is a way to manage runtime errors using try and except so the program continues running smoothly.


