# Library Management System - OOP Style

class Book:
	"""Creates object Book"""

	def __init__(self,
				book_id,
				book_title,
				book_author,
				available_copies):
		"""Initialize book with it's nessary attributes"""
		self.book_id = book_id
		self.book_title = book_title
		self.book_author = book_author
		self.total_copies = available_copies
		self.available_copies = available_copies

	def increase_book(self, amount = 1):
		"""Add amount to total copies"""
		self.available_copies += amount

	def decrease_book(self, amount = 1):
		"""Remove amount from total copies"""
		self.available_copies -= amount

class Member:
	"""Create object Member"""

	def __init__(self,
				member_id,
				member_name,
				member_email):
		"""Initialize member with it's nessary attributes"""
		self.member_id = member_id
		self.member_name = member_name
		self.member_email = member_email
		self.borrowed_book_list = []

	def add_borrowed_book_list(self, added_book):
		"""Add the borrowed book to member borrowed book list"""
		self.borrowed_book_list.append(added_book)

	def remove_borrowed_book_list(self, book):
		"""Remove the following book from member borrowed book list"""
		self.borrowed_book_list.remove(book)

class Library:
	"""Storing book and member list, do all the methods"""

	def __init__(self, book_list = [], member_list = []):
		"""Initialize the Libary with book and member list"""
		self.book_list = book_list
		self.member_list = member_list
		self.transaction_list = []

	def add_books(self, book):
		"""Add a new book to the library"""
		self.book_list.append(book)
		print(f"Book '{book.book_title}' added successfully!")

	def add_member(self, member):
		"""Register a new library member"""
		self.member_list.append(member)
		print(f"Member '{member.member_name}' registered successfully!")

	def find_book(self, book_id):
		"""Find a book by ID"""
		for book in self.book_list:
			if book.book_id == book_id:
				return book
		return None

	def find_member(self, member_id):
		"""Find a member by ID"""
		for member in self.member_list:
			if member.member_id == member_id:
				return member
		return None

	def borrow_book(self, member_id, book_id):
		"""Process a book borrowing transaction"""
		member = self.find_member(member_id)
		book = self.find_book(book_id)

		if not member:
			print("Error: Member not found!")
			return False

		if not book:
			print("Error: Book not found!")
			return False

		if book.available_copies <= 0:
			print("Error: No copies avaliable!")
			return False

		if len(member.borrowed_book_list) >= 3:
			print("Error: Member has reached borrowing limit!")
			return False

		#Process the borrowing
		book.available_copies -= 1
		member.add_borrowed_book_list(book)

		transaction = {
			'member_id': member_id,
			'book_id': book_id,
			'member_name': member.member_name,
			'book_title': book.book_title
		}
		self.transaction_list.append(transaction)

		print(f"{member.member_name} borrowed '{book.book_title}'")
		return True

	def return_book(self, member_id, book_id):
		"""Process a book return transaction"""
		member = self.find_member(member_id)
		book = self.find_book(book_id)

		if not member or not book:
			print("Error: Member or book not found!")
			return False

		if book_id not in [book.book_id for book in member.borrowed_book_list]:
			print("Error: This member hasn't borrowed this book!")
			return False

		# Process the return
		book.available_copies += 1
		member.remove_borrowed_book_list(book)

		# Remove from borrowed_books list
		for i, transaction in enumerate(self.transaction_list):
			if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
				self.transaction_list.pop(i)
				break

		print(f"{member.member_name} returned '{book.book_title}'")
		return True

	def display_available_books(self):
		"""Display all books with available copies"""
		print("\n=== Available Books ===")
		for book in self.book_list:
			if book.available_copies > 0:
				print(f"{book.book_title} by {book.book_author} - {book.available_copies} copies avaliable")

	def display_member_books(self, member_id):
		"""Display books borrowed by a specific member"""
		member = self.find_member(member_id)
		if not member:
			print("Error: Member not found!")
			return

		print(f"\n=== Books borrowed by {member.member_name} ===")
		if not member.borrowed_book_list:
			print("No books currently borrowed")
		else:
			for book in member.borrowed_book_list:
				print(f"- {book.book_title} by {book.book_author}")


if __name__ == "__main__":
	main_library = Library()
	main_library.add_books(Book(1, "Kun Shu and Jackie", "Kun Shu", 3))
	main_library.add_books(Book(2, "Ant the Little Monster", "Nattanan", 2))
	main_library.add_books(Book(3, "Attack On Titan", "Hajime Isayama", 1))
	main_library.add_books(Book(4, "HELP ME WITH OOP PLEASE", "GOD", 2))

	main_library.add_member(Member(101, "Kun Shu", "shuu@email.com"))
	main_library.add_member(Member(102, "Big Nice", "niceverybig@email.com"))
	main_library.add_member(Member(103, "Fussy Fuse", "fuse@email.com"))

	main_library.borrow_book(101, 1)		# Kun Shu borrows Kun Shu and Jackie
	main_library.borrow_book(101, 2)		# Kun Shu borrows At the Little Monster
	main_library.borrow_book(102, 1)		# Big Nice borrows Kun Shu and Jackie

	main_library.display_member_books(101)	# Kun Shu's books
	main_library.display_member_books(102)	# Big Nice's books
	main_library.display_member_books(103)	# Fussy Fuse's books
