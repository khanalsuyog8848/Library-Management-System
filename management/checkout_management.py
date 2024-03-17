class CheckoutManager:
    def __init__(self, storage_handler):
        self.storage = storage_handler

    def checkout_book(self, user_id, isbn):
        if self.is_book_available(isbn):
            self.storage.checkout_book(user_id, isbn)
            print(f"Book with ISBN {isbn} checked out by user {user_id}.")
        else:
            print(f"Book with ISBN {isbn} is not available for checkout.")

    def checkin_book(self, isbn):
        self.storage.checkin_book(isbn)
        print(f"Book with ISBN {isbn} checked in successfully.")

    def is_book_available(self, isbn):
        books = self.storage.database._read_data(self.storage.database.books_file)
        for book in books:
            if book['isbn'] == isbn:
                return book['available']
        return False  

    def list_checkouts(self):
        self.storage.list_checkouts()
