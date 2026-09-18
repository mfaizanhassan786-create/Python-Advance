
## Simple code:

# num = int (input("Enter a number: ") )
# print(10/num)


## Using try-except:

# try:
#     num = int(input("Enter a number: "))
#     print(10/num)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input")
# except Exception as e:
#     print(f"An unexpected error occurrred : {e}")


# try:
#     print("Running code...")
# except:
#     print("Error Found!!!")
# else:
#     print("Code is running successfully")
# finally:
#     print("Code is terminated")
    


age = -3
if age < 0:
    raise ValueError("Age cannot be negative")