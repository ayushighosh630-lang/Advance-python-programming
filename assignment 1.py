# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'"{self.title}" has been borrowed.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not borrowed.')


# Patron Class
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def display_borrowed_books(self):
        print(f"\nBorrowed Books by {self.name}:")
        if not self.borrowed_books:
            print("None")
        else:
            for book in self.borrowed_books:
                print("-", book.title)


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added successfully.')

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron "{patron.name}" registered successfully.')

    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if not book.is_borrowed:
                book.borrow()
                patron.borrow_book(book)
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid Patron ID or ISBN.")

    def return_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if book.is_borrowed:
                book.return_book()
                patron.return_book(book)
            else:
                print("Book is already available.")
        else:
            print("Invalid Patron ID or ISBN.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} | {book.author} | ISBN: {book.isbn} | {status}")

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons:
            print(f"Name: {patron.name}, ID: {patron.patron_id}")
            patron.display_borrowed_books()


# ---------------- Main Program ----------------

library = Library()

# Add Books
book1 = Book("Python Programming", "Guido van Rossum", "101")
book2 = Book("Data Structures", "Mark Allen", "102")
book3 = Book("Operating Systems", "Galvin", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register Patrons
patron1 = Patron("Ayushi", 1)
patron2 = Patron("Rahul", 2)

library.register_patron(patron1)
library.register_patron(patron2)

# Display Books
library.display_books()

# Borrow Book
print("\nBorrowing a Book...")
library.borrow_book(1, "101")

# Display Books
library.display_books()

# Return Book
print("\nReturning a Book...")
library.return_book(1, "101")

# Display Books
library.display_books()

# Display Patrons
library.display_patrons()