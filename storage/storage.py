from datetime import datetime
from models import Book, User, Checkout, LibraryDatabase


class StorageHandler:
    def __init__(self, db_path):
        """
        Initializes a StorageHandler object with a database path.

        Args:
            db_path (str): The path to the directory where database files will be stored.
        """
        self.database = LibraryDatabase(db_path)

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        book = Book(title, author, isbn)
        self.database.add_book(book)

    def add_user(self, name, user_id):
        """
        Adds a new user to the library database.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        user = User(name, user_id)
        self.database.add_user(user)

    def checkout_book(self, user_id, isbn):
        """
        Checks out a book for a user and updates its availability.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        checkout = Checkout(user_id, isbn)
        self.database.add_checkout(checkout)
        self.update_book_availability(isbn, False)

    def checkin_book(self, isbn):
        """
        Checks in a book and updates its availability and return date.

        Args:
            isbn (str): The ISBN of the book being checked in.
        """
        self.update_book_availability(isbn, True)
        checkouts = self.database._read_data(self.database.checkouts_file)
        for checkout in checkouts:
            if checkout["isbn"] == isbn and checkout["return_date"] is None:
                checkout["return_date"] = datetime.now().strftime("%Y-%m-%d")
                break
        self.database._write_data(self.database.checkouts_file, checkouts)

    def update_book_availability(self, isbn, availability):
        """
        Updates the availability status of a book in the database.

        Args:
            isbn (str): The ISBN of the book.
            availability (bool): The availability status of the book.
        """
        books = self.database._read_data(self.database.books_file)
        for book in books:
            if book["isbn"] == isbn:
                book["available"] = availability
                break
        self.database._write_data(self.database.books_file, books)

    def list_books(self):
        """Lists all books in the library database."""
        books = self.database._read_data(self.database.books_file)
        for book in books:
            print(book)

    def list_users(self):
        """Lists all users in the library database."""
        users = self.database._read_data(self.database.users_file)
        for user in users:
            print(user)

    def list_checkouts(self):
        """Lists all checkouts in the library database."""
        checkouts = self.database._read_data(self.database.checkouts_file)
        for checkout in checkouts:
            print(checkout)
