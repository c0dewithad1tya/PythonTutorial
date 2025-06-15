'''
Welcome to File Operations
This is a test file to demonstrate file operations in Python.
Functions:
- open: Open a file
    Arguments:
        - file_path: Path to the file
        - mode: Mode in which to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending, 'x' for creating a new file)
        - encoding: Encoding to use for the file (e.g., 'utf-8')
- read: Read the contents of a file
- write: Write to a file
- close: Close a file
'''

# Read the contents of the file
f = open("C:\\python_dev\\FileOps\\test_file.txt", "r")
data = f.read()
print(data)
f.close()

# Write to the file
f = open("C:\\python_dev\\FileOps\\test_file.txt", "w")
f.write("And Hello Arnav!")
f.close()

# Append to the file
f = open("C:\\python_dev\\FileOps\\test_file.txt", "a+")
f.write(" and Hello Aditya!")
f.seek(0)  # return to the top of the file
text = f.read()
print(text)
f.close()

# Replace the contents of the file
actual_text = 'Hello'
replace_text = 'Hi'

f = open("C:\\python_dev\\FileOps\\test_file.txt", "r")
data = f.read()

f = open("C:\\python_dev\\FileOps\\test_file.txt", "w")
f.write(data.replace(actual_text, replace_text))
f.close()

# Create a new file
f = open("C:\\python_dev\\FileOps\\new_test_file.txt", "x")
f.write("This is a new test file.")
f.close()

# Clear the contents of the file
open("C:\\python_dev\\FileOps\\new_test_file.txt", "w").close()