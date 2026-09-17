
# Polymorphism basically means
# that a function can take more than one form. Like a single function could be used
# 

# class Dog:
#     def speak(self):
#         print("Woof!")

# class Cat:
#     def speak(self):
#         print("Meow!")

# for pet in [Dog(), Cat()]:
#     pet.speak()


# Another Example:

# class vehicle:
#     def move(self):
#         print("some movement is done")

# class car(vehicle):
#     def move(self):
#         print("car is moving on road")

# class boat(vehicle):
#     def move(self):
#         print("Boat is moving on water")

# car1 = car()
# boat1 = boat()


# Another Example:

class Calculator:
    def add(self, a, b=0, c=0):
        return a+b+c

cal = Calculator()
print(cal.add(5))
print(cal.add(10,20))
print(cal.add(10,20,30))


