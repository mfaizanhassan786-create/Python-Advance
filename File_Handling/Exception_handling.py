

# with open("missing.txt", "r") as file:
#     print(file.read())

# print(file)
## This is used when the file is not found ##

# try :
#     with open("missing.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
    
# else:
#     print("File is read successfully")


filename = "my_info.txt"
name = "GitHub Copilot"
age = 1

# Try to read existing file; if missing, create it with name and age, then read.

try:
    with open(filename, "r") as file:
        print(fin.read())

except FileNotFoundError:
    with open(filename, "w") as fout:
        fout.write(f"{name}\n {age}\n")
    with open(filename, "r") as fin:
      print(fin.read())
