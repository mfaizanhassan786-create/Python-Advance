#In this file we are going to learn about the classes in python 
#In this file we are disscuss about the Problems.

## Practice no. 01

# class Car:
#     def drive(self, name):
#         print(f"Driving {name}")


## Practice no. 02

# car1 = Car()
# car1.drive("BMW")

# class Car:
#     color = "red"
#     def drive (self):
#         print(f"{self.color} car is moving!")


# car1 = Car()

# car1.drive()


## Practice no. 03

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



## Practice no. 04

# class Dog:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} is barking!")
    
#     def get_age(self):
#         print(f"{self.name} is {self.age} years old!")

# dog1 = Dog("Boddy", "10")
# dog1.bark()
# dog1.get_age()


## Instance Variables and Methods:
# instance variables and instance methods are belong to the objects.
# class variables and class methods are belong to the class.
# static variables and static methods are belong to the class.

## Practice no. 01

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age       # This will now receive an integer number
#         self.grade = grade

    
#     # def get_name(self):
#     #     print(self.name)
    
#     # def get_age(self):
#     #     print(self.age)
    
#     # def get_grade(self):
#     #     print(self.grade)
    
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}")

#     def is_eligible(self):
#         # Make sure this checks self.age, not self.grade!
#         if self.age >= 18:
#             print(f"{self.name} is eligible for voting")
#         else:
#             print(f"{self.name} is not eligible for voting")

# # Creating Objects (Notice: NO quotes around the age numbers!)
# student1 = Student("Faizan", 20, "A")
# student2 = Student("Bilal", 15, "B")
# student3 = Student("Ali", 25, "C")

# # Accessing attributes (Notice: we use comma ',' instead of '+' to print numbers)
# print("Name : " + student1.name)
# print("Age :", student1.age)
# print("Grade : " + student1.grade)

# # Calling Methods
# print("\n")
# student1.display()
# student2.display()
# student3.display()

# print("\n--- Voting Eligibility ---")
# student1.is_eligible()
# student2.is_eligible()
# student3.is_eligible()
