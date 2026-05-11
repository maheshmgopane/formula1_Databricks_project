"""
FILE HANDLING IN PYTHON
========================
A comprehensive guide on file handling, methods, file types, and best practices.
"""

# 1. WHAT IS FILE HANDLING?
# =========================
# File handling is the process of working with files (create, read, update, delete).
# Python has built-in functions for creating, reading, updating, and deleting files.


# 2. WAYS TO HANDLE FILES
# =======================
path= "/Users/hp/source/repos/Python/formula1_Databricks_project/.venv/Advance_Python/example.txt"
# METHOD 1: Using open() and close()
# -----------------------------------
'''
def method1_open_close():
    """Traditional way - manual open and close"""
    file = open(path, "r")
    content = file.read()
    file.close()
    return content
result=method1_open_close()
print(result)

# METHOD 2: Using with statement (Context Manager) - RECOMMENDED
# ---------------------------------------------------------------
def method2_context_manager():
    """Recommended way - automatically closes file"""
    with open(path, "r") as file:
        content = file.read()
    return content
result=method2_context_manager()
print(result)

# METHOD 3: Reading line by line
# -------------------------------
def method3_read_lines():
    """Read file line by line"""
    with open(path, "r") as file:
        for line in file:
            print(line.strip())

method3_read_lines()

# METHOD 4: Using readlines()
# ----------------------------
def method4_readlines():
    """Read all lines as list"""
    with open(path, "r") as file:
        lines = file.readlines()
    return lines
result=method4_readlines()
print(result)
'''
# METHOD 5: Writing to file
# --------------------------
def method5_write_file():
    """Write content to file"""
    with open(path, "w") as file:
        file.write("Hello, World!/n")
        file.write("This is a new line.")

result=method5_write_file()
print(result)
'''
# METHOD 6: Appending to file
# ----------------------------
def method6_append_file():
    """Append content to existing file"""
    with open("output.txt", "a") as file:
        file.write("/nAppended line")


# 3. FILE MODES
# =============
"""
'r'   - Read (default). Opens file for reading, error if not exists
'a'   - Append. Opens file for appending, creates if not exists
'w'   - Write. Opens file for writing, creates/overwrites file
'x'   - Create. Creates file, error if exists
'b'   - Binary mode (e.g., 'rb', 'wb')
't'   - Text mode (default, e.g., 'rt', 'wt')
"""


# 4. TYPES OF FILES CAN HANDLE
# =============================

# TEXT FILES (.txt)
# -----------------
def handle_text_file():
    """Handle plain text files"""
    with open("file.txt", "r") as file:
        content = file.read()
    return content


# CSV FILES (.csv)
# ----------------
import csv

def handle_csv_file():
    """Handle CSV files"""
    with open("data.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


def write_csv_file():
    """Write to CSV file"""
    data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
    with open("data.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)


# JSON FILES (.json)
# ------------------
import json

def handle_json_file():
    """Handle JSON files"""
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def write_json_file():
    """Write to JSON file"""
    data = {"name": "John", "age": 30, "city": "New York"}
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# BINARY FILES (.bin, .exe, .jpg, .png)
# --------------------------------------
def handle_binary_file():
    """Handle binary files"""
    with open("image.jpg", "rb") as file:
        binary_data = file.read()
    return binary_data


def copy_binary_file():
    """Copy binary file"""
    with open("source.jpg", "rb") as source:
        with open("copy.jpg", "wb") as destination:
            destination.write(source.read())


# EXCEL FILES (.xlsx)
# -------------------
# Requires: pip install openpyxl
def handle_excel_file():
    """Handle Excel files"""
    try:
        from openpyxl import load_workbook
        workbook = load_workbook("data.xlsx")
        sheet = workbook.active
        for row in sheet.iter_rows(values_only=True):
            print(row)
    except ImportError:
        print("openpyxl not installed")


# PICKLE FILES (.pkl)
# --------------------
import pickle

def handle_pickle_file():
    """Handle pickle files (Python serialization)"""
    data = {"key": "value", "list": [1, 2, 3]}
    with open("data.pkl", "wb") as file:
        pickle.dump(data, file)


def read_pickle_file():
    """Read pickle file"""
    with open("data.pkl", "rb") as file:
        data = pickle.load(file)
    return data


# 5. BEST PRACTICES FOR FILE HANDLING
# ====================================

"""
1. ALWAYS USE 'with' STATEMENT
   - Automatically closes file
   - Handles exceptions gracefully
   
2. USE APPROPRIATE FILE MODES
   - 'r' for reading, 'w' for writing, 'a' for appending
   - Use 'b' for binary files
   
3. HANDLE EXCEPTIONS
   - Use try-except for file operations
   - Catch specific exceptions like FileNotFoundError
   
4. USE ABSOLUTE/RELATIVE PATHS CORRECTLY
   - Use os.path.join() for cross-platform compatibility
   - Use pathlib.Path for modern approach
   
5. CLOSE FILES PROPERLY
   - The 'with' statement ensures this
   - Prevents resource leaks
   
6. READ LARGE FILES IN CHUNKS
   - Don't load entire large files into memory
   - Use iteration or chunking
   
7. ENCODE/DECODE CORRECTLY
   - Specify encoding (e.g., 'utf-8')
   - Handle encoding errors
   
8. VALIDATE FILE EXISTENCE
   - Check if file exists before operations
   - Use os.path.exists() or pathlib
   
9. USE APPROPRIATE ENCODINGS
   - UTF-8 is commonly used
   - Consider encoding for non-ASCII characters
"""


# BEST PRACTICE EXAMPLES
# =======================

import os
from pathlib import Path

def best_practice_read():
    """Best practice: Read file safely"""
    file_path = "example.txt"
    
    # Check if file exists
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    return None


def best_practice_write():
    """Best practice: Write file safely"""
    file_path = "output.txt"
    data = "Hello, World!"
    
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)
        print(f"File written successfully to {file_path}")
    except IOError as e:
        print(f"Error writing file: {e}")


def best_practice_read_large_file():
    """Best practice: Read large files in chunks"""
    file_path = "large_file.txt"
    chunk_size = 1024  # 1KB chunks
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                process_chunk(chunk)
    except FileNotFoundError:
        print(f"File {file_path} not found")


def process_chunk(chunk):
    """Process a chunk of data"""
    pass


def best_practice_using_pathlib():
    """Best practice: Using pathlib for modern file handling"""
    file_path = Path("example.txt")
    
    # Check if file exists
    if file_path.exists():
        # Read file
        content = file_path.read_text(encoding="utf-8")
        return content
    
    # Write file
    file_path.write_text("Hello, World!", encoding="utf-8")


def best_practice_csv_handling():
    """Best practice: Handle CSV files safely"""
    file_path = "data.csv"
    
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                process_row(row)
    except FileNotFoundError:
        print(f"File {file_path} not found")
    except Exception as e:
        print(f"Error: {e}")


def process_row(row):
    """Process a CSV row"""
    pass


def best_practice_json_handling():
    """Best practice: Handle JSON files safely"""
    file_path = "data.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
    except json.JSONDecodeError:
        print("Invalid JSON format")
    except Exception as e:
        print(f"Error: {e}")


# SUMMARY TABLE
# ==============
"""
FILE TYPE    | EXTENSION | MODE | LIBRARY/APPROACH
---------------------------------------------------
Text         | .txt      | r/w  | open()
CSV          | .csv      | r/w  | csv module
JSON         | .json     | r/w  | json module
Binary       | .bin      | rb/wb| open() in binary
Image        | .jpg/.png | rb/wb| open() in binary
Excel        | .xlsx     | r/w  | openpyxl
Python Obj   | .pkl      | rb/wb| pickle module
XML          | .xml      | r/w  | xml module
"""
'''