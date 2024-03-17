from storage import StorageHandler

class BookManager:
    def __init__(self, storage_handler):
        self.storage = storage_handler

    def add_book(self, title, author, isbn):
        self.storage.add_book(title, author, isbn)
        print(f"Book '{title}' added successfully.")

    def update_book(self, isbn, title=None, author=None):
        books = self.storage.database._read_data(self.storage.database.books_file)
        updated = False
        for book in books:
            if book['isbn'] == isbn:
                if title:
                    book['title'] = title
                if author:
                    book['author'] = author
                updated = True
                break
        if updated:
            self.storage.database._write_data(self.storage.database.books_file, books)
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def delete_book(self, isbn):
        books = self.storage.database._read_data(self.storage.database.books_file)
        books = [book for book in books if book['isbn'] != isbn]
        self.storage.database._write_data(self.storage.database.books_file, books)
        print(f"Book with ISBN {isbn} deleted successfully.")

    def list_books(self):
        self.storage.list_books()

    def search_books(self, **kwargs):
        books = self.storage.database._read_data(self.storage.database.books_file)
        results = books
        for key, value in kwargs.items():
            results = [book for book in results if book.get(key, '').lower() == value.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found matching the search criteria.")
