# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book for easy reading."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the Book that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    # Creating a Book instance
    my_book = Book("1984", "George Orwell", 1949)

    # String representation (__str__)
    print(str(my_book))  # Output: 1984 by George Orwell, published in 1949

    # Official representation (__repr__)
    print(repr(my_book))  # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the book object to invoke __del__
    del my_book


