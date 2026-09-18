# # Special Fnctions:
# # Methods
# # Functions

# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"

# b = Book("Python", "Faizan", 100)
# print(b)
    
    
# #Another Example:
# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __len__(self):
#         return len(self.songs)

#     def __add__(self, other):
#         # Combines both playlist names and merges both song lists
#         return Playlist(self.name + " & " + other.name, self.songs + other.songs)

# # FIXED: Added names ("Chill Mix" and "Gym Beats") as the first argument
# p1 = Playlist("Chill Mix", ["Song1", "Song2", "Song3"])
# p2 = Playlist("Gym Beats", ["Song4", "Song5", "Song6"])

# # This prints the number of songs in p1 (3)
# print(len(p1))

# # This merges p1 and p2 using the __add__ method, then counts all songs (6)
# print(len(p1 + p2))



# #Another Example:

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __add__(self, other):
#         if not isinstance(other, Point):
#             return TypeError("Operand must be a Point")
#         return Point(self.x + other.x, self.y + other.y)

# p1 = Point(1, 2)
# p2 = Point(3, 4)

# print((p1 + p2).x, (p1 + p2).y)


# #Comparisons Method:
# #Aother Example:

# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"

#     def __lt__(self,other):
#         if not isinstance(other, Book):
#             return TypeError("Operand must be a Book")
#         return self.pages < other.pages

#     def __le__(self,other):
#         if not isinstance(other, Book):
#             return TypeError("Operand must be a Book")
#         return self.pages <= other.pages

#     def __gt__(self,other):
#         if not isinstance(other, Book):
#             return TypeError("Operand must be a Book")
#         return self.pages > other.pages

#     def __ge__(self,other):
#         if not isinstance(other, Book):
#             return TypeError("Operand must be a Book")
#         return self.pages >= other.pages


# b1 = Book("Python", "Faizan", 100)
# b2 = Book("Java", "Faizan", 200)

# print(b1 < b2)
# print(b1 <= b2)
# print(b1 > b2)
# print(b1 >= b2)
