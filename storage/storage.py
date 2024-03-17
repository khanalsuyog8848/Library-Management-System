from datetime import datetime
from models import Book, User, Checkout, LibraryDatabase

class StorageHandler:
    def __init__(self, db_path):
        self.database = LibraryDatabase(db_path)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.database.add_book(book)

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.database.add_user(user)

    def checkout_book(self, user_id, isbn):
        checkout = Checkout(user_id, isbn)
        self.database.add_checkout(checkout)
        self.update_book_availability(isbn, False)

    def checkin_book(self, isbn):
        self.update_book_availability(isbn, True)
        checkouts = self.database._read_data(self.database.checkouts_file)
        for checkout in checkouts:
            if checkout['isbn'] == isbn and checkout['return_date'] is None:
                checkout['return_date'] = datetime.now().strftime('%Y-%m-%d')
                break  
        self.database._write_data(self.database.checkouts_file, checkouts)


    def update_book_availability(self, isbn, availability):
        books = self.database._read_data(self.database.books_file)
        for book in books:
            if book['isbn'] == isbn:
                book['available'] = availability
                break
        self.database._write_data(self.database.books_file, books)

    def list_books(self):
        books = self.database._read_data(self.database.books_file)
        for book in books:
            print(book)

    def list_users(self):
        users = self.database._read_data(self.database.users_file)
        for user in users:
            print(user)

    def list_checkouts(self):
        checkouts = self.database._read_data(self.database.checkouts_file)
        for checkout in checkouts:
            print(checkout)
