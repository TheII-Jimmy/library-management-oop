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
				member_email,
				borrowed_book_list = []):
		"""Initialize member with it's nessary attributes"""
		self.member_id = member_id
		self.member_name = member_name
		self.member_email = member_email
		self.borrowed_book_list = borrowed_book_list

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

	def add_books(self):
		"""Add a new book to the library"""
		pass

	def add_member(self):
		"""Register a new library member"""
		pass

	def find_book(self):
		"""Find a book by ID"""
		pass

	def find_member(self):
		"""Find a member by ID"""
		pass

	def borrow_book(self):
		"""Process a book borrowing transaction"""
		pass

	def return_book(self):
		"""Process a book return transaction"""
		pass

	def display_avaliable_books(self):
		"""Display all books with available copies"""
		pass

	def display_member_books(self):
		"""Display books borrowed by a specific member"""
		pass
