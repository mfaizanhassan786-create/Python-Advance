# In this file we are discuss about the Reading and writing the data.

## Reading Formating 

# file = open("File_Handling/demo.txt", "r")

# print(file.read())

# file.close()

## writing Formating

# file = open("demo.txt", "w")

# file.write("Hello, this is a new line")

# file.close()


file1 = open("demo.txt", "a")
file1.write("\nHello, this is second new line and I am writing this line using a")
file1.close()