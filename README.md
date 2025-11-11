# Library Management System (OOP)

## Project Overview

This project is a simple Library Management System implemented in Python using Object-Oriented Programming (OOP) principles. It allows for managing book and member databases, and processing borrowing and returning transactions.

## Project Structure

The project is organized into two main versions: a procedural implementation and an OOP solution.

This is the structure of this project

- **`libary-namagement-oop/`**: The main folder of this project
	- **`README.md`**: # This file

	- **`procedural_version/`**: Procedural style version of the program
		- **`libary_procedural.py`**: # Original procedural code
		- **`test_procedural.py`**: # Comprehensive test suite

	- **`oop_solution/`**: OOP style version of the program
		- **`libary_oop.py`**: # My own OOP implementation
		- **`test_oop.py`**: # Tests for OOP version

## Design Overview

The OOP solution is built around three core classes: `Book`, `Member`, and `Library`.

### Class: `Book`

Represents a single book in the library's catalog.

* **Attributes:**
    * `book_id` (int): A unique identifier for the book.
    * `book_title` (str): The title of the book.
    * `book_author` (str): The author of the book.
    * `total_copies` (int): The total number of copies owned by the library.
    * `available_copies` (int): The number of copies currently available to borrow.
* **Key Methods:**
    * `increase_book(amount=1)`: Increases the `available_copies` (e.g., when a book is returned).
    * `decrease_book(amount=1)`: Decreases the `available_copies` (e.g., when a book is borrowed).

### Class: `Member`

Represents a single registered library member.

* **Attributes:**
    * `member_id` (int): A unique identifier for the member.
    * `member_name` (str): The member's name.
    * `member_email` (str): The member's email address.
    * `borrowed_book_list` (list): A list containing the `Book` objects the member has currently borrowed.
* **Key Methods:**
    * `add_borrowed_book_list(added_book)`: Adds a `Book` object to the member's `borrowed_book_list`.
    * `remove_borrowed_book_list(book)`: Removes a `Book` object from the member's `borrowed_book_list`.

### Class: `Library`

The main class that manages the entire system. It holds the lists of books and members and orchestrates all transactions.

* **Attributes:**
    * `book_list` (list): A list of all `Book` objects in the library.
    * `member_list` (list): A list of all `Member` objects registered in the library.
    * `transaction_list` (list): A list of dictionaries tracking current loans.
* **Key Methods:**
    * `add_books(book)`: Adds a new `Book` object to the `book_list`.
    * `add_member(member)`: Adds a new `Member` object to the `member_list`.
    * `find_book(book_id)`: Finds and returns a `Book` object by its ID.
    * `find_member(member_id)`: Finds and returns a `Member` object by its ID.
    * `borrow_book(member_id, book_id)`: Manages a member borrowing a book. Includes all validation checks (e.g., member/book exists, copies are available, member has not reached borrow limit).
    * `return_book(member_id, book_id)`: Manages a member returning a book. Includes validation to ensure the member actually borrowed the book.
    * `display_available_books()`: Prints a list of all books with > 0 available copies.
    * `display_member_books(member_id)`: Prints a list of books currently borrowed by a specific member.

## Testing

A comprehensive test suite is provided in `test_oop.py`. It covers all class methods and library operations, including basic operations and edge cases.

### 1. Book Class Tests (Tests 1-2)

```python
# From test_oop.py
book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
book2 = Book(2, "Clean Code", "Robert Martin", 2)
```
Tests the following:
- Increasing available copies (```increase_book()```).
- Decreasing available copies (```decrease_book()```).

### 2. Member Class Tests (Tests 3-4)

```python
# From test_oop.py
member = Member(101, "Alice Smith", "alice@email.com")
member.add_borrowed_book_list(book1)
```
Tests the following:
- Adding a book to a member's personal borrowed list (```add_borrowed_book_list()```).
- Removing a book from a member's personal borrowed list (```remove_borrowed_book_list()```).

### 3. Library Class Tests (Tests 5-18)

```python
# From test_oop.py
main_library = Library()
main_library.add_books(Book(1, "Kun Shu and Jackie", "Kun Shu", 3))
main_library.add_member(Member(101, "Kun Shu", "shuu@email.com"))
```
Tests the following:
- Basic Operations:
	- Adding books and registering members (`add_books()`, `add_member()`).
	- Processing successful borrow and return transactions (`borrow_book()`, `return_book()`).
	- Displaying available books and a member's borrowed books (`display_available_books()`, `display_member_books()`).
- Edge Cases & Error Handling:
	- Attempting to borrow a book that is unavailable (0 copies).
	- Attempting to borrow a book when the member has reached the borrowing limit (3 books).
	- Attempting to return a book the member has not borrowed.
	- Using non-existent `book_id` or `member_id` for transactions.

## How to Run the Test Code

To run the comprehensive test suite for the OOP version, navigate to the `libary-management-oop/` directory and run the `test_oop.py` file:

```bash
python oop_solution/test_oop.py
```
This will execute all 18 test cases and print the results to the console.
To run the procedural version, execute `test_procedural.py`:
