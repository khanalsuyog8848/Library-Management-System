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


### management
Contains the logic for managing books, users, and checkouts.

### models
Defines the data models for books, users, and checkouts.

### storage
Handles data storage, retrieval, and manipulation for the system.

### utils
Provides utility functions, including logging.

### main.py
The entry point of the application, presenting a menu-driven interface to the user.

## Getting Started

### Prerequisites
- Python 3.x

### Installation and Running the code
Clone the repository to your local machine:

```bash
git clone https://github.com/khanalsuyog8848/Library-Management-System.git
cd library-management-system
python main.py







