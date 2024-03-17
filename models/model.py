from datetime import datetime
import json
import os


class Book:
    def __init__(self, title, author, isbn):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def to_dict(self):
        """
        Converts Book object to a dictionary.

        Returns:
            dict: Dictionary representation of the Book object.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
        }


class User:
    def __init__(self, name, user_id):
        """
        Initializes a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The unique identifier of the user.
        """
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        """
        Converts User object to a dictionary.

        Returns:
            dict: Dictionary representation of the User object.
        """
        return {"name": self.name, "user_id": self.user_id}


class Checkout:
    def __init__(self, user_id, isbn, checkout_date=None, return_date=None):
        """
        Initializes a Checkout object.

        Args:
            user_id (str): The user ID associated with the checkout.
            isbn (str): The ISBN of the book being checked out.
            checkout_date (str, optional): The date when the book is checked out. Defaults to current date.
            return_date (str, optional): The date when the book is returned. Defaults to None.
        """
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = (
            checkout_date if checkout_date else datetime.now().strftime("%Y-%m-%d")
        )
        self.return_date = return_date

    def to_dict(self):
        """
        Converts Checkout object to a dictionary.

        Returns:
            dict: Dictionary representation of the Checkout object.
        """
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "checkout_date": self.checkout_date,
            "return_date": self.return_date,
        }


class LibraryDatabase:
    def __init__(self, db_path):
        """
        Initializes a LibraryDatabase object.

        Args:
            db_path (str): The path to the directory where database files will be stored.
        """
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
        self.books_file = os.path.join(self.db_path, "books.json")
        self.users_file = os.path.join(self.db_path, "users.json")
        self.checkouts_file = os.path.join(self.db_path, "checkouts.json")
        self._init_files()

    def _init_files(self):
        """
        Initializes database files if they do not exist.
        """
        for file_path in [self.books_file, self.users_file, self.checkouts_file]:
            if not os.path.exists(file_path):
                with open(file_path, "w") as file:
                    json.dump([], file)

    def _read_data(self, file_path):
        """
        Reads data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            list: The data read from the file.
        """
        with open(file_path, "r") as file:
            return json.load(file)

    def _write_data(self, file_path, data):
        """
        Writes data to a JSON file.

        Args:
            file_path (str): The path to the JSON file.
            data (list): The data to write to the file.
        """
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self, book: Book):
        """
        Adds a book to the library database.

        Args:
            book (Book): The Book object to add to the database.
        """
        books = self._read_data(self.books_file)
        books.append(book.to_dict())
        self._write_data(self.books_file, books)

    def add_user(self, user: User):
        """
        Adds a user to the library database.

        Args:
            user (User): The User object to add to the database.
        """
        users = self._read_data(self.users_file)
        users.append(user.to_dict())
        self._write_data(self.users_file, users)

    def add_checkout(self, checkout: Checkout):
        """
        Adds a checkout record to the library database.

        Args:
            checkout (Checkout): The Checkout object representing the checkout record.
        """
        checkouts = self._read_data(self.checkouts_file)
        checkouts.append(checkout.to_dict())
        self._write_data(self.checkouts_file, checkouts)
