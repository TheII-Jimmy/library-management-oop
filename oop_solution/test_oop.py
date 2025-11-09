from library_oop import Book, Member, Library

def test_libary_system():
	"""Comprehensive test of all library functions"""

	print("=" * 60)
	print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
	print("=" * 60)

	print("TEST BOOK CLASS:")
	# Test 1: Increasing Avaliable Books
	print("\n--- TEST 1: Increasing Avaliable Books ---")
	book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
	book2 = Book(2, "Clean Code", "Robert Martin", 2)
	print("book1 ava copies = 3")
	book1.increase_book()
	print("book1 increase 1 (defult value)")
	print("book1 avaliable copies: ", book1.available_copies)
	print("book2 ava copies = 2")
	book2.increase_book(2)
	print("book2 increase 2")
	print("book2 avaliable copies: ", book2.available_copies)

	# Test 2: Decreasing Avaliable Books
	print("\n--- TEST 2: Decreasing Avaliable Books ---")
	book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
	book2 = Book(2, "Clean Code", "Robert Martin", 2)
	print("book1 ava copies = 3")
	book1.decrease_book()
	print("book1 decrease 1 (defult value)")
	print("book1 avaliable copies: ", book1.available_copies)
	print("book2 ava copies = 2")
	book2.decrease_book(2)
	print("book1 decrease 2")
	print("book2 avaliable copies: ", book2.available_copies)




if __name__ == "__main__":
	test_libary_system()
