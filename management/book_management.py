class BookManager:
    def __init__(self, storage_handler):
        """
        Initializes a BookManager object with a storage handler.

        Args:
            storage_handler: An instance of StorageHandler for interacting with the database.
        """
        self.storage = storage_handler

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library database.

        Args:
            title: The title of the book.
            author: The author of the book.
            isbn: The ISBN (International Standard Book Number) of the book.
        """
        self.storage.add_book(title, author, isbn)
        print(f"Book '{title}' added successfully.")

    def update_book(self, isbn, title=None, author=None):
        """
        Updates the information of an existing book in the library database.

        Args:
            isbn: The ISBN of the book to update.
            title: (Optional) The new title of the book.
            author: (Optional) The new author of the book.
        """
        books = self.storage.database._read_data(self.storage.database.books_file)
        updated = False
        for book in books:
            if book["isbn"] == isbn:
                if title:
                    book["title"] = title
                if author:
                    book["author"] = author
                updated = True
                break
        if updated:
            self.storage.database._write_data(self.storage.database.books_file, books)
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def delete_book(self, isbn):
        """
        Deletes a book from the library database.

        Args:
            isbn: The ISBN of the book to delete.
        """
        books = self.storage.database._read_data(self.storage.database.books_file)
        books = [book for book in books if book["isbn"] != isbn]
        self.storage.database._write_data(self.storage.database.books_file, books)
        print(f"Book with ISBN {isbn} deleted successfully.")

    def list_books(self):
        """Lists all books available in the library database."""
        self.storage.list_books()

    def search_books(self, **kwargs):
        """
        Searches for books in the library database based on specified criteria.

        Args:
            **kwargs: Arbitrary keyword arguments representing search criteria (e.g., title, author).

        Note:
            The search is case-insensitive and supports partial matches.

        Returns:
            None. Prints matching books or a message if no books are found.
        """
        books = self.storage.database._read_data(self.storage.database.books_file)
        results = books
        for key, value in kwargs.items():
            results = [
                book for book in results if book.get(key, "").lower() == value.lower()
            ]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found matching the search criteria.")
