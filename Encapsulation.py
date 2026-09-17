
#Encapluation in python

class Student:
    def __init__ (self, age, name, grade, course):
        self.__grade = grade #Private Attribute
student1 = Student(20, "Faizan", "A", "Computer Science")
# print(student1.__grade) # It will give error as the grade is private attribute

# To access the private attribute we use getters and setters