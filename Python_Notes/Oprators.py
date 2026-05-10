#python oprators
#Arithmetic Operators   return a new value based on the arithmetic operation performed on the operands.
a=10
b=5
print(a+b)  # addition returns the sum of a and b. If either operand is a float, the result will be a float.
print(a-b)  # subtraction returns the difference of a and b. If either operand is a float, the result will be a float.
print(a*b)  # multiplication  returns the product of a and b. If either operand is a float, the result will be a float.
print(a/b)  # division removes the fractional part and returns the quotient as an integer. If either operand is a float, the result will be a float.
print(a//b) # floor division returns the largest integer less than or equal to the quotient. If either operand is a float, the result will be a float.
print(a%b)  # modulus   returns the remainder of the division of a by b. If either operand is a float, the result will be a float.
print(a**b) # exponentiation    returns a raised to the power of b. If either operand is a float, the result will be a float.
#Comparison Operators return a boolean value based on the comparison of two values.
print(a==b)  # equal to returns True if a and b are equal, and False otherwise.
print(a!=b)  # not equal to   returns True if a and b are not equal, and False otherwise. 
print(a> b)  # greater than returns True if a is greater than b, and False otherwise.
print(a< b)  # less than returns True if a is less than b, and False otherwise.
print(a>=b)  # greater than or equal to returns True if a is greater than or equal to b, and False otherwise.
print(a<=b)  # less than or equal to returns True if a is less than or equal to b, and False otherwise.
#logical operators return a boolean value based on the logical relationship between two or more expressions.
x = True
y = False
print(x and y)  # Output: False returns True if both x and y are True, and False otherwise.
print(x or y)   # Output: True returns True if either x or y is True, and False otherwise.
print(not x)    # Output: False returns True if x is False, and False if x is True.

#Pemdas rule: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)
print(10 + 5 * 2)  # Output: 20 returns 10 plus the product of 5 and 2, which is 20.
print((10 + 5) * 2)  # Output: 30 returns the sum of 10 and 5, which is 15, multiplied by 2, which is 30.
#Assignment Operators 
# assignment operators are used to assign values to variables. They can also be used to perform an operation on a variable and assign the result back to the same variable.
x = 10
x += 5  # equivalent to x = x + 5, which assigns the value of x plus 5 back to x. After this operation, x will be 15.
x -= 3  # equivalent to x = x - 3, which assigns the value of x minus 3 back to x. After this operation, x will be 12.
x *= 2  # equivalent to x = x * 2, which assigns the value of x multiplied by 2 back to x. After this operation, x will be 24.
x /= 4  # equivalent to x = x / 4, which assigns the value of x divided by 4 back to x. After this operation, x will be 6.0.
x //= 2 # equivalent to x = x // 2, which assigns the value of x floor divided by 2 back to x. After this operation, x will be 3.0.
x %= 2  # equivalent to x = x % 2, which assigns the value of x modulus 2 back to x. After this operation, x will be 1.0.
x **= 3 # equivalent to x = x ** 3, which assigns the value of x raised to the power of 3 back to x. After this operation, x will be 1.0.       
#identity operators
#identity operators are used to compare the memory locations of two objects. They return True if the objects being compared are the same object in memory, and False otherwise.
a = [1, 2, 3]   
b = a            # b is assigned the same list object as a, so a and b refer to the same object in memory.
c = [1, 2, 3]   # c is assigned a new list object with the same contents as a, but it is a different object in memory.
print(a is b)   # Output: True returns True because a and b refer to the same object in memory.
print(a is c)   # Output: False returns False because a and c refer to different objects in memory, even though they have the same contents.
print(a == c)   # Output: True returns True because a and c have the same contents, even though they are different objects in memory.       

#membership operators
#membership operators are used to test whether a value is present in a sequence (such as a string, list, or tuple) or a collection (such as a set or dictionary). They return True if the value is found in the sequence or collection, and False otherwise.
my_list = [1, 2, 3, 4, 5]           
print(3 in my_list)   # Output: True returns True because 3 is an element of my_list.
print(6 in my_list)   # Output: False returns False because 6 is not an element of my_list.
print(3 not in my_list)   # Output: False returns False because 3 is an element of my_list.
print(6 not in my_list)   # Output: True returns True because 6 is not an element of my_list.   




