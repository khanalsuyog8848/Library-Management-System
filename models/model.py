from datetime import datetime
import json
import os

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }

class Checkout:
    def __init__(self, user_id, isbn, checkout_date=None, return_date=None):
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = checkout_date if checkout_date else datetime.now().strftime('%Y-%m-%d')
        self.return_date = return_date

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "checkout_date": self.checkout_date,
            "return_date": self.return_date
        }

class LibraryDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
        self.books_file = os.path.join(self.db_path, "books.json")
        self.users_file = os.path.join(self.db_path, "users.json")
        self.checkouts_file = os.path.join(self.db_path, "checkouts.json")
        self._init_files()

    def _init_files(self):
        for file_path in [self.books_file, self.users_file, self.checkouts_file]:
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    json.dump([], file)

    def _read_data(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def _write_data(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_book(self, book: Book):
        books = self._read_data(self.books_file)
        books.append(book.to_dict())
        self._write_data(self.books_file, books)

    def add_user(self, user: User):
        users = self._read_data(self.users_file)
        users.append(user.to_dict())
        self._write_data(self.users_file, users)

    def add_checkout(self, checkout: Checkout):
        checkouts = self._read_data(self.checkouts_file)
        checkouts.append(checkout.to_dict())
        self._write_data(self.checkouts_file, checkouts)
