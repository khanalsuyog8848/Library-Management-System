class CheckoutManager:
    def __init__(self, storage_handler):
        """
        Initializes a CheckoutManager object with a storage handler.

        Args:
            storage_handler: An instance of StorageHandler for interacting with the database.
        """
        self.storage = storage_handler

    def checkout_book(self, user_id, isbn):
        """
        Checks out a book for a user if it is available.

        Args:
            user_id: The ID of the user checking out the book.
            isbn: The ISBN of the book to be checked out.
        """
        if self.is_book_available(isbn):
            self.storage.checkout_book(user_id, isbn)
            print(f"Book with ISBN {isbn} checked out by user {user_id}.")
        else:
            print(f"Book with ISBN {isbn} is not available for checkout.")

    def checkin_book(self, isbn):
        """
        Checks in a book, making it available for checkout again.

        Args:
            isbn: The ISBN of the book to be checked in.
        """
        self.storage.checkin_book(isbn)
        print(f"Book with ISBN {isbn} checked in successfully.")

    def is_book_available(self, isbn):
        """
        Checks if a book is available for checkout.

        Args:
            isbn: The ISBN of the book to check availability.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        books = self.storage.database._read_data(self.storage.database.books_file)
        for book in books:
            if book["isbn"] == isbn:
                return book["available"]
        return False

    def list_checkouts(self):
        """Lists all book checkouts."""
        self.storage.list_checkouts()
