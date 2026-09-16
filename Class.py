#In this file we are going to learn about the classes in python 
#In this file we are disscuss about the Problems.



# class Car:
#     def drive(self, name):
#         print(f"Driving {name}")


# car1 = Car()
# car1.drive("BMW")

class Car:
    color = "red"
    def drive (self):
        print(f"{self.color} car is moving!")


car1 = Car()

car1.drive()




# class Car:
#     def __init__(self, color, name):
#         self.name = name
#         self.color = color
    
#     def start_engine(self):
#         print(f"Engine started {self.name} and {self.color}")

# # First object of the class Car
# car1 = Car("red", "BMW")
# car2 = Car("blue", "Audi")

# car1.start_engine()
# car2.start_engine()

# # Second Object

# myfriend = Car("green", "Toyota")
# myfriend.start_engine()



