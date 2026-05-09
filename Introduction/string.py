#what is string in python
#A string in Python is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are immutable, meaning they cannot be changed after they are created. They can contain letters, numbers, symbols, and whitespace. Strings are commonly used for storing and manipulating text data in Python. 
#String operations include concatenation, slicing, and various string methods for manipulating and formatting strings.
#whaat is character in python
#A character in Python is a single unit of text, represented as a string of length one. It can be a letter, digit, symbol, or whitespace. Characters are used to build strings and can be accessed using indexing. For example, in the string "Hello", 'H' is a character at index 0, 'e' is at index 1, and so on. Characters can also be represented using their Unicode code points, such as '\u0041' for 'A'. 

#character operations   
char1 = 'A'
char2 = 'B'
print(char1)  # Output: A
print(char2)  # Output: B
print(char1 + char2)  # Output: AB

#3 charectorstic of string1. Immutable: Strings in Python cannot be changed after they are created. Any operation that modifies a string will create a new string instead of altering the original one.
#2. Ordered: The characters in a string are ordered, meaning they have a specific sequence. You can access individual characters using their index, starting from 0 for the first character.
#3. Iterable: Strings can be iterated over, allowing you to loop through each character in the string using a for loop or other iteration methods.
#string indexing and slicing
#positive indexing starts from 0 and goes up to n-1, where n is the length of the string. Negative indexing starts from -1 for the last character and goes backwards to -n for the first character. Slicing allows you to extract a portion of the string by specifying a range of indices. The syntax for slicing is string[start:end], where start is the index of the first character to include and end is the index of the first character to exclude.
#negative indexing and slicing 
my_string = "Hello, World!" 
print(my_string[0])  # Output: H
print(my_string[7])  # Output: W
print(my_string[-1])  # Output: !
print(my_string[0:5])  # Output: Hello
print(my_string[7:])  # Output: World!
#string operations
str1 = "Hello"  
str2 = "World"
print(str1 + " " + str2)  # Output: Hello World
print(str1 * 3)  # Output: HelloHelloHello  
#length of string
my_string = "Hello, World!" 
print(len(my_string))  # Output: 13
#check password length
password = "my_secure_password" 
if len(password) >= 8:
    print("Password is strong.")
#string slice and step
my_string = "Hello, World!"     
print(my_string[::2])  # Output: Hlo ol!
print(my_string[1::2])  # Output: el,Wrd

number='10'
print('' + number * 10)  # Output: 10
#string concatenation and repetition
#String methods are built-in functions that can be called on string objects to perform various operations. Some common string methods include:
#example of string methods
name="Alice"
print(name.upper())  # Output: ALICE
print(name.lower())  # Output: alice
print(name.capitalize())  # Output: Alice
#string membership testing
#String membership testing allows you to check if a specific substring is present within a string. You can use the 'in' keyword to perform this check. It returns True if the substring is found and False otherwise.
#example of string membership testing
my_string = "Hello, World!"
print("Hello" in my_string)  # Output: True
print("Python" in my_string)  # Output: False

print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!   
print(my_string.capitalize())  # Output: Hello, world!
print(my_string.title())  # Output: Hello, World!   #title() method capitalizes the first letter of each word in the string.
print(my_string.strip())  # Output: Hello, World! (removes leading and trailing whitespace)
print(my_string.swapcase())  # Output: hELLO, wORLD! (swaps the case of each character in the string)
print(my_string.replace("Hello", "Hi"))  # Output: Hi, World! (replaces "Hello" with "Hi")
print(my_string.split(", "))  # Output: ['Hello', 'World!'] (splits the string into a list based on the delimiter ", ")
print(my_string.join(["Hi", "Everyone"]))  # Output: HiHello, World!Everyone (joins the list of strings using the original string as a separator)
print(my_string.find("World"))  # Output: 7 (returns the index of the first occurrence of "World")
print(my_string.count("o"))  # Output: 2 (counts the number of occurrences of "o" in the string)
print(my_string.startswith("Hello"))  # Output: True (checks if the string starts with "Hello")
print(my_string.endswith("!"))  # Output: True (checks if the string ends with "!")
print(my_string.isalpha())  # Output: False (checks if all characters in the string are alphabetic)
print(my_string.isdigit())  # Output: False (checks if all characters in the string are digits)
print(my_string.isalnum())  # Output: False (checks if all characters in the string are alphanumeric)
print(my_string.islower())  # Output: False (checks if all characters in the string are lowercase)
print(my_string.isupper())  # Output: False (checks if all characters in the string are uppercase)
print(my_string.isspace())  # Output: False (checks if all characters in the string are whitespace)
print(my_string.center(20, "*"))  # Output: ***Hello, World!*** (centers the string within a field of width 20, using "*" as the fill character)
print(my_string.ljust(20, "-"))  # Output: Hello, World!------- (left-justifies the string within a field of width 20, using "-" as the fill character)
print(my_string.rjust(20, "."))  # Output: .......Hello, World
print(my_string.zfill(20))  # Output: 0000000Hello, World! (pads the string with zeros on the left to fill a width of 20)
print(my_string.partition(", "))  # Output: ('Hello', ', ', 'World!') (partitions the string into three parts based on the first occurrence of the delimiter ", ")
print(my_string.rpartition(", "))  # Output: ('Hello', ', ', 'World!') (partitions the string into three parts based on the last occurrence of the delimiter ", ")
print(my_string.splitlines())  # Output: ['Hello, World!'] (splits the string into a list of lines based on newline characters)

#String formatting allows you to create formatted strings by embedding expressions inside string literals. You can use f-strings (formatted string literals) or the format() method for string formatting.
#example of string formatting
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.  



