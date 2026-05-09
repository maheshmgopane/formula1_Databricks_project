"""numeric types: int, float, complex
int: whole numbers, positive or negative, without decimals, of unlimited length.
float: numbers that contain a decimal point, or are in exponential (E) notation.    
complex: numbers with a real and imaginary part, represented as a + bj, where a is 
the real part and b is the imaginary part. The imaginary part is denoted by 'j' in Python."""
print(type(10))        # int
print(type(3.14))      # float          
print(type(2 + 3j))   # complex

'''boolean type: bool
bool: represents one of two values: True or False. It is often used in conditional statements'''
print(type(True))   # bool
print(type(False))  # bools

'''None type: NoneType
None: represents the absence of a value or a null value. It is often used to indicate that a variable has no value or 
to signify the end of a list or other data structure.'''
print(type(None))   # NoneType
'''
sequence types: str, list, tuple
str: represents a sequence of characters, enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are immutable, meaning they cannot be changed after they are created.
list: represents an ordered collection of items, enclosed in square brackets ([ ]). Lists are mutable, meaning they can be changed after they are created.
tuple: represents an ordered collection of items, enclosed in parentheses (( )). Tuples are immutable, meaning they cannot be changed after they are created.'''
print(type("Hello, World!"))  # str     
print(type([1, 2, 3, 4, 5]))  # list
print(type((1, 2, 3, 4, 5)))  # tuple   

'''set types: set, frozenset
set: represents an unordered collection of unique items, enclosed in curly braces ({ }). Sets are mutable, meaning they can be changed after they are created.
frozenset: represents an unordered collection of unique items, enclosed in curly braces ({ }). Frozensets are immutable, meaning they cannot be changed after they are created.'''
print(type({1, 2, 3, 4, 5}))  # set
print(type(frozenset({1, 2, 3, 4, 5})))  # frozenset   
'''     
mapping type: dict
dict: represents a collection of key-value pairs, enclosed in curly braces ({ }). Each key is unique and maps to a value. Dictionaries are mutable, meaning they can be changed after they are created.'''
print(type({'name': 'Alice', 'age': 30, 'city': 'New York'}))  # dict      