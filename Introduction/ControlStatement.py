# Control Statements in Python
# Control statements are used to control the flow of execution in a program. They allow you to make decisions, repeat actions, and handle exceptions. The main types of control statements in Python are:
# 1. Conditional Statements (if, elif, else)    
# 2. Looping Statements (for, while)
# 3. Control Flow Statements (break, continue, pass)   
# Example of conditional statements

age = int(input("Enter your age: "))    # Get user input and convert it to an integer
#area of circle
radius = float(input("Enter the radius of the circle: "))  # Get user input and convert it to a float
pi = 3.14159
area = pi * radius ** 2
print("The area of the circle is:", area)
##check if a number is positive, negative, or zero
number = float(input("Enter a number: "))# Get user input and convert it to a float
if number > 0:# Check if the number is greater than zero
    print("The number is positive.")# Check if the number is less than zero
elif number < 0:# If the number is less than zero, it is negative
    print("The number is negative.")  # If the number is not greater than zero and not less than zero, it must be zero
else:    print("The number is zero.")# Check if the age is greater than or equal to 18
if age >= 18:# If the age is 18 or older, the person is an adult
    print("You are an adult.") 
else: # If the age is less than 18, the person is a minor
    print("You are a minor.")   
# Example of looping statements
# Print numbers from 1 to 5 using a for loop
for i in range(1, 6):# The range function generates numbers from 1 to 5 (6 is exclusive)
    print(i)# Print numbers from 1 to 5 using a while loop
# Print numbers from 1 to 5 using a while loop
i = 1# Initialize the variable i to 1
while i <= 5:# Continue the loop as long as i is less than or equal to 5
    print(i)# Print the current value of i
    i += 1# Increment i by 1 to move to the next number
# Example of control flow statements
# Using break to exit a loop
for i in range(1, 10):# Loop through numbers from 1 to 9
    if i == 5:# If i is equal to 5, break out of the loop
        break# Print the current value of i (this will print numbers from 1 to 4)
    print(i) 
# Using continue to skip an iteration
for i in range(1, 10):# Loop through numbers from 1 to 9
    if i % 2 == 0:# If i is even, skip the rest of the loop and continue with the next iteration
        continue# Print the current value of i (this will print only odd numbers from 1 to 9)
    print(i)# Using pass to do nothing
# Using pass as a placeholder
for i in range(1, 10):# Loop through numbers from 1 to 9
    if i % 2 == 0:# If i is even, do nothing
        pass  # This will do nothing for even numbers
    else:# If i is odd, print the number
        print(i)


