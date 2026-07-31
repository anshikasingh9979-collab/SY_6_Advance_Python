class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print(title, "book added successfully.")

    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(name, "registered successfully.")

    def borrow_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in self.books:
                    if book.title == book_title and book.available:
                        book.available = False
                        patron.borrowed_books.append(book)
                        print(patron_name, "borrowed", book_title)
                        return
        print("Book not available or patron not found.")

    def return_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in patron.borrowed_books:
                    if book.title == book_title:
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print(patron_name, "returned", book_title)
                        return
        print("Book not found.")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            if book.available:
                print(book.title, "- Available")
            else:
                print(book.title, "- Borrowed")


library = Library()

library.add_book("Python")
library.add_book("Java")
library.add_book("C++")

library.register_patron("Anshika")
library.register_patron("Rahul")

library.borrow_book("Anshika", "Python")

library.display_books()

library.return_book("Anshika", "Python")

library.display_books()