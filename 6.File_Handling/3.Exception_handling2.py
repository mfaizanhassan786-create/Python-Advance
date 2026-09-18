
## Simple code:
# num = int (input("Enter a number: ") )
# print(10/num)


## Using try-except:
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
except Exception as e:
    print(f"An unexpected error occurrred : {e}")
    