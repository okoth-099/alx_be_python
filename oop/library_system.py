# library_system.py

# Base class: Book
class Book:
    def __init__(self, title, author):
        """Initialize the book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of the book."""
        return f"Book: {self.title} by {self.author}"


# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size_kb):
        """Initialize the EBook with title, author, and file size in KB."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size_kb = file_size_kb  # Unique attribute for EBook

    def __str__(self):
        """String representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size_kb}KB"


# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Unique attribute for PrintBook

    def __str__(self):
        """String representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition: Library
class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)

