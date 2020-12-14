# cass inheritance diagram:
#
#        object
#       /      \
#     Book    User
#


class Book(object):
    """Create a new e-book."""

    def __init__(self, name, price, publisher):
        """Return a new book instance."""
        self.name = name
        self.price = price
        self.publisher = publisher

    def __str__(self):
        """print book info."""
        return f"{self.name} - {self.price} - {self.publisher}"


class User(object):

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.books = []

    def buy(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def read(self, book):
        """read purchased books."""
        print('read books')
