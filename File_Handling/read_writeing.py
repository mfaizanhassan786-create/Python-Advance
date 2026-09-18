# In this file we are discuss about the Reading and writing the data.

## Reading Formating 

# file = open("File_Handling/demo.txt", "r")

# print(file.read())

# file.close()

## writing Formating

# file = open("demo.txt", "w")

# file.write("Hello, this is a new line")

# file.close()


## Appending Formating:

# file1 = open("demo.txt", "a")

# file1.write("\nHello, this is second new line and I am writing this line using a")

# file1.close()


## Context Manager:

## open method:

# with open("demo.txt", "r") as file:

#     print(file.read())
# # It is closing the file automatically.

## tempfile method:

# import tempfile

# temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)

# temp_file.write("Hello, this is a new line")

# temp_file.close()


## Zipfile Method:

# import zipfile

# with zipfile.ZipFile("demo.zip", "w") as zip_file:

#     zip_file.write("demo.txt")

#     print("File zipped successfully!")


## pathlib method:

from pathlib import Path

path = Path("demo.txt")

path.write_text("Hello, this is a new line")
 