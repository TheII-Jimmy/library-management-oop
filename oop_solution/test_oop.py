from library_oop import Book, Member, Library

def test_libary_system():
	"""Comprehensive test of all library functions"""

	print("=" * 60)
	print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
	print("=" * 60)

	print("\n=== TEST BOOK CLASS ===")

	# Test 1: Increasing Avaliable Books
	print("\n--- TEST 1: Increasing Avaliable Books ---")
	book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
	book2 = Book(2, "Clean Code", "Robert Martin", 2)
	print(f"book1 increase from {book1.available_copies} by 1")
	book1.increase_book()
	print("book1 avaliable copies: ", book1.available_copies)
	print(f"book2 increase from {book2.available_copies} by 2")
	book2.increase_book(2)
	print("book2 avaliable copies: ", book2.available_copies)

	# Test 2: Decreasing Avaliable Books
	print("\n--- TEST 2: Decreasing Avaliable Books ---")
	book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
	book2 = Book(2, "Clean Code", "Robert Martin", 2)
	print("book1 ava copies = 3")
	print(f"book1 decrease from {book1.available_copies} by 1")
	book1.decrease_book()
	print("book1 avaliable copies: ", book1.available_copies)
	print(f"book1 decrease from {book1.available_copies} by 2")
	book2.decrease_book(2)
	print("book2 avaliable copies: ", book2.available_copies)

	print("\n=== TEST MEMBER CLASS ===")

	# Test 3: add book to borrow book list
	print("\n--- TEST 3: Add Book to borrow book list ---")
	book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
	book2 = Book(2, "Clean Code", "Robert Martin", 2)
	member = Member(101, "Alice Smith", "alice@email.com")
	member.add_borrowed_book_list(book1)
	print("added book1:", book1.book_title)
	print([i.book_title for i in member.borrowed_book_list])
	member.add_borrowed_book_list(book2)
	print("added book2:", book2.book_title)
	print([i.book_title for i in member.borrowed_book_list])

	# Test 4: remove book from borrow book list (used the same list as before)
	print("\n--- TEST 4: Remove Book from borrow book list ---")
	print([i.book_title for i in member.borrowed_book_list])
	member.remove_borrowed_book_list(book1)
	print("remove book1:", book1.book_title)
	print([i.book_title for i in member.borrowed_book_list])
	member.remove_borrowed_book_list(book2)
	print("remove book2:", book2.book_title)
	print([i.book_title for i in member.borrowed_book_list])



if __name__ == "__main__":
	test_libary_system()
