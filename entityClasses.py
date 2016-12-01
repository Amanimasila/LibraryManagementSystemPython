__author__ = 'mrinal'

import datetime

class Librarian(object):
	"""Entity class for librarians"""
	def __init__(self, firstName, lastName, email, address, city, phNo):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.address = address
		self.city = city
		self.phNo = phNo
		self.id = createLibrarianId(firstName, lastName)
		self.password = createPassword(firstName, lastName)


	def createLibrarianId(self, firstName, lastName):
		return firstName[:4] + lastName[:4]

	def createPassword(self, firstName, lastName):
		return firstName[len(firstName) - 2:] + lastName[len(lastName) - 2:]


class Book(object):
	"""Entity class for books"""
	def __init__(self, callNo, name, author, publisher, quantity, issued):
		self.callNo = callNo
		self.name = name
		self.author = author
		self.publisher = publisher
		self.quantity = quantity
		self.issued = issued
		self.addedDate = datetime.datetime.now().strftime("%Y-%m-%d")
		self.id = createBookId(name, author)

	def createBookId(self, name, author):
		return name[:4] + author[:4]
		