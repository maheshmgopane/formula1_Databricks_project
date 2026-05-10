"""
File handling in Python:
- Open files using built-in open() function.
- Read, write, or append to files.
- Close files when done or use with statement.

Types of files:
- Text files (default mode, e.g. .txt, .csv)
- Binary files (mode 'rb', 'wb', 'ab', e.g. images, audio, custom binary formats)

Basic file handling examples:

# Text file read
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Text file write
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, Python file handling!\n')

# Text file append
with open('example.txt', 'a', encoding='utf-8') as f:
    f.write('Append a new line.\n')

# Binary file write
with open('example.bin', 'wb') as f:
    f.write(b'\x00\x01\x02')

# Binary file read
with open('example.bin', 'rb') as f:
    data = f.read()

# File modes:
# 'r'  : read (default)
# 'w'  : write (truncate)
# 'a'  : append
# 'x'  : create and write, fail if exists
# 'b'  : binary mode
# 't'  : text mode (default)
# '+'  : read and write

# Always prefer 'with' to ensure files are closed automatically.
"""

# Additional examples of file opening patterns

def open_file_read(path):
    """Open a text file for reading."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def open_file_write(path, text):
    """Open a text file for writing (truncates existing file)."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def open_file_append(path, text):
    """Open a text file for appending."""
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text)


def open_file_exclusive(path, text):
    """Open a file for exclusive creation; fail if already exists."""
    with open(path, 'x', encoding='utf-8') as f:
        f.write(text)


def open_binary_read(path):
    """Open a binary file for reading."""
    with open(path, 'rb') as f:
        return f.read()


def open_binary_write(path, data):
    """Open a binary file for writing."""
    with open(path, 'wb') as f:
        f.write(data)


def open_read_write(path):
    """Open a file for both reading and writing."""
    with open(path, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0)
        f.write('# Updated\n')
        return content

path="/Users/hp/source/repos/Python/formula1_Databricks_project/Sample.txt"
data=open_file_read(path)
data.show