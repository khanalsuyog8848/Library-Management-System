import os
from storage import StorageHandler
from management import *
from utils import setup_logger

logger = setup_logger('library_management_system', 'library_management_system.log')

db_path = "library_data"
storage_handler = StorageHandler(db_path)
book_manager = BookManager(storage_handler)
user_manager = UserManager(storage_handler)
checkout_manager = CheckoutManager(storage_handler)

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Books")
    print("5. Search Books")
    print("6. Add User")
    print("7. Update User")
    print("8. Delete User")
    print("9. List Users")
    print("10. Search Users")
    print("11. Checkout Book")
    print("12. Checkin Book")
    print("13. Exit")
    choice = input("Enter choice: ")
    return choice

def search_criteria():
    print("\nSearch by:")
    print("1. Title")
    print("2. Author")
    print("3. ISBN")
    print("4. Name")
    print("5. User ID")
    choice = input("Enter search criteria: ")
    return choice

def main():
    logger.info("Library Management System started")
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            logger.info(f"Book added: {title}, {author}, {isbn}")
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            book_manager.update_book(isbn, title, author)
            logger.info(f"Book updated: {isbn}")
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            logger.info(f"Book deleted: {isbn}")
        elif choice == '4':
            book_manager.list_books()
        elif choice == '5':
            criteria = search_criteria()
            if criteria in ['1', '2', '3']:
                value = input("Enter search value: ")
                if criteria == '1':
                    book_manager.search_books(title=value)
                elif criteria == '2':
                    book_manager.search_books(author=value)
                elif criteria == '3':
                    book_manager.search_books(isbn=value)
                logger.info(f"Search performed for books with criteria: {criteria} = {value}")
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            logger.info(f"User added: {name}, {user_id}")
        elif choice == '7':
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            user_manager.update_user(user_id, name)
            logger.info(f"User updated: {user_id}")
        elif choice == '8':
            user_id = input("Enter user ID to delete: ")
            user_manager.delete_user(user_id)
            logger.info(f"User deleted: {user_id}")
        elif choice == '9':
            user_manager.list_users()
        elif choice == '10':
            criteria = search_criteria()
            if criteria in ['4', '5']:
                value = input("Enter search value: ")
                if criteria == '4':
                    user_manager.search_users(name=value)
                elif criteria == '5':
                    user_manager.search_users(user_id=value)
                logger.info(f"Search performed for users with criteria: {criteria} = {value}")
        elif choice == '11':
            user_id = input("Enter user ID for checkout: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
            logger.info(f"Book checked out: {isbn} by user {user_id}")
        elif choice == '12':
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_manager.checkin_book(isbn)
            logger.info(f"Book checked in: {isbn}")
        elif choice == '13':
            logger.info("Exiting Library Management System")
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")
            logger.warning("Invalid choice made in menu")

if __name__ == "__main__":
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    main()
