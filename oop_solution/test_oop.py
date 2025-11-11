from library_oop import Book, Member, Library

def test_libary_system():
	"""Comprehensive test of all library functions"""

	main_library = Library()

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
	print("book1 available copies: ", book1.available_copies)
	print(f"book2 increase from {book2.available_copies} by 2")
	book2.increase_book(2)
	print("book2 available copies: ", book2.available_copies)

	# Test 2: Decreasing Avaliable Books
	print("\n--- TEST 2: Decreasing Avaliable Books ---")
	book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
	book2 = Book(2, "Clean Code", "Robert Martin", 2)
	print("book1 ava copies = 3")
	print(f"book1 decrease from {book1.available_copies} by 1")
	book1.decrease_book()
	print("book1 available copies: ", book1.available_copies)
	print(f"book1 decrease from {book1.available_copies} by 2")
	book2.decrease_book(2)
	print("book2 available copies: ", book2.available_copies)

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

	print("\n=== TEST LIBRARY CLASS ===")

	# Test 5: Add Books
	print("\n--- Test 5: Adding Books ---")
	main_library.add_books(Book(1, "Kun Shu and Jackie", "Kun Shu", 3))
	main_library.add_books(Book(2, "Ant the Little Monster", "Nattanan", 2))
	main_library.add_books(Book(3, "Attack On Titan", "Hajime Isayama", 1))
	main_library.add_books(Book(4, "HELP ME WITH OOP PLEASE", "GOD", 2))

	# Test 6: Add Members
	print("\n--- TEST 6: Registering Members ---")
	main_library.add_member(Member(101, "Kun Shu", "shuu@email.com"))
	main_library.add_member(Member(102, "Big Nice", "niceverybig@email.com"))
	main_library.add_member(Member(103, "Fussy Fuse", "fuse@email.com"))

	# Test 7: Display Avaliable Books
	print("\n--- TEST 7: Display Available Books ---")
	main_library.display_available_books()

	# Test 8: Successful Book Borrowing
	print("\n--- TEST 8: Successful Borrowing ---")
	main_library.borrow_book(101, 1)		# Kun Shu borrows Kun Shu and Jackie
	main_library.borrow_book(101, 2)		# Kun Shu borrows At the Little Monster
	main_library.borrow_book(102, 1)		# Big Nice borrows Kun Shu and Jackie

	# Test 9: Display Member's Borrowed Books
	print("\n--- TEST 9: Display Member's Books ---")
	main_library.display_member_books(101)	# Kun Shu's books
	main_library.display_member_books(102)	# Big Nice's books
	main_library.display_member_books(103)	# Fussy Fuse's books

	# Test 10: Display Avilable Books After Borrowing
	print("\n--- TEST 10: Available Books After Borrowing ---")
	main_library.display_available_books()

	# Test 11: Borrow Last Available Copy
	print("\n--- TEST 11: Borrowing Last Copy ---")
	main_library.borrow_book(103, 3)		# Fussy Fuse borrow the only copy of AOT
	main_library.display_available_books()

	# Test 12: Try to Borrow Unavailable Book
	print("\n--- TEST 12: Attempting to Borrow Unavailable Book ---")
	main_library.borrow_book(102, 3)		# Big Nice tries to borrow unavailable book

	# Test 13: Borrowing Limit Test
	print("\n--- TEST 13: Testing Borrowing Limit (3 books max) ---")
	main_library.borrow_book(101, 4)		# Kun Shu's 3rd book
	main_library.display_member_books(101)
	main_library.borrow_book(101, 3)		# Kun Shu tries to borrow 4th book (should fail)

	# Test 14: Return Books
	print("\n--- TEST 14: Returning Books ---")
	main_library.return_book(101, 1)		# Kun Shu returns Kun Shu and Jackie
	main_library.return_book(102, 1)		# Big Nice returns Kun Shu and Jackie
	main_library.display_member_books(101)
	main_library.display_available_books()

	# Test 15: Try to Return Book Not Borrowed
	print("\n--- TEST 15: Attempting Invalid Return ---")
	main_library.return_book(102, 2)		# Big Nice tries to return book he didn't borrow

	# Test 16: Return and Borrow Again
	print("\n--- TEST 16: Return and Re-borrow ---")
	main_library.return_book(103, 3)		# Fussy Fuse returns AOT
	main_library.borrow_book(102, 3)		# Big Nice borrows it
	main_library.display_member_books(102)

	# Test 17: Error Cases - Non-existent Member/Book
	print("\n--- TEST 17: Error Handling ---")
	main_library.borrow_book(999, 1)			# Non-existent member
	main_library.borrow_book(101, 999)		# Non-existent book
	main_library.return_book(999, 1)			# Non-existent member
	main_library.display_member_books(999)	# Non-existent member

	# Test 18: Final Status
	print("\n--- TEST 18: Final Library Status ---")
	print("\nAll Borrowed Books:")
	for transaction in main_library.transaction_list:
		print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
	
	print("\nAll Members and Their Books:")
	for member in main_library.member_list:
		print(f"\n{member.member_name} ({member.member_id}):")
		if member.borrowed_book_list:
			for book_id in [book.book_id for book in member.borrowed_book_list]:
				book = main_library.find_book(book_id)
				print(f"  - {book.book_title}")
		else:
			print("  (No books borrowed)")
	
	main_library.display_available_books()

	print("\n" + "=" * 60)
	print("TEST COMPLETE")
	print("=" * 60)

if __name__ == "__main__":
	test_libary_system()
