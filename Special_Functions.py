# Special Fnctions:
# Methods
# Functions

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"

b = Book("Python", "Faizan", 100)
print(b)
    
    