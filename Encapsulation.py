# #Encapluation in python

# class Student:
#     def __init__(self, age, name, grade, course):
#         self.age = age
#         self.name = name
#         self.__grade = grade # Private Attribute
#         self.course = course

#     # To access the private attribute we use getters and setters
#     def get_grade(self):
#         return self.__grade

#     def set_grade(self, grade):
#         self.__grade = grade

# student1 = Student(20, "Faizan", "A", "Computer Science")
# # print(student1.__grade) # It will give error as the grade is private attribute

# # Accessing private attribute through getter
# print("Student Grade:", student1.get_grade())

# #Another Example:
# #Example of the Getters and Setters.

# class Student:
#     @property
#     def grade(self):
#         return self.__grade

#     def __init__(self, age, name, grade, course):
#         # self.age = age
#         # self.name = name
#         self.__grade = grade # Private Attribute
#         # self.course = course
#     def get_grade(self):
#         return self.__grade
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Invalid grade")

# student1 = Student(20, "Faizan", "A", "Computer Science")
# student1.set_grade(90)
# print(student1.get_grade())