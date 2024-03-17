# Library Management System (LMS)
 Contains the modular redesigned code from the assignment.



## Overview
The Library Management System is a comprehensive tool designed for managing books, users, and book checkouts in a library environment. Built in Python, this system allows for the addition, update, deletion, and searching of books and users, as well as managing book checkouts and returns.

## Features
- **Book Management:** Add, update, delete, list, and search books using title, author, or ISBN.
- **User Management:** Add, update, delete, list, and search users.
- **Checkout Management:** Checkout and checkin books for users, with the ability to list all current checkouts.

## Project Structure
The project is organized into several directories, each serving a specific function within the LMS:

```
.
├── management
│ ├── init.py
│ ├── book_management.py
│ ├── user_management.py
│ └── checkout_management.py
├── models
│ ├── init.py
│ └── model.py
├── storage
│ ├── init.py
│ └── storage.py
├── utils
│ ├── init.py
│ └── logger.py
└── main.py
```


### Components
#### Management Modules
- **Book Management (management/book_management.py):** Handles book-related operations, including adding, updating, deleting, and searching for books within the library's database.

- **User Management (management/user_management.py):** Manages user-related tasks, such as adding, updating, and deleting users. Also supports searching for users based on specific criteria.

- **Checkout Management (management/checkout_management.py):** Manages the checkout process, including checking books out to users, checking them in, and listing current checkouts. Ensures that books are marked as available or unavailable as appropriate.

#### Models
- **Book (models/model.py):** Represents a book with properties like title, author, ISBN, and availability status.

- **User (models/model.py):** Represents a user with properties like name and user ID.

- **Checkout (models/model.py):** Represents a checkout record, including user ID, ISBN of the checked-out book, checkout date, and return date.

#### Storage
- **Storage Handler (storage/storage.py):** Acts as the intermediary between the management modules and the library database. It performs the actual data handling tasks, such as adding books or users to the database and updating book availability.

#### Utilities
- **Logger (utils/logger.py):** Provides logging functionality to track operations and changes within the system. Helps in debugging and auditing system use.

#### Main Script
- **Main (main.py):** The entry point of the application. Provides a command-line interface for interacting with the Library Management System. It initializes the storage handler and management modules and processes user inputs to perform various operations.


## Getting Started

### Prerequisites
- Python 3.x

### Installation and Running the code
Clone the repository to your local machine:

```shell
git clone https://github.com/khanalsuyog8848/Library-Management-System.git
cd library-management-system
python main.py
```







