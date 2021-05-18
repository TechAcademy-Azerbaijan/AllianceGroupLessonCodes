

class Library:
    books = []

    def __add__(self, new_book):
        self.books.append(new_book)

    def __sub__(self, removed_book):
        self.books.remove(removed_book)

    def __repr__(self):
        return ','.join(self.books)

    def __str__(self):
        return ','.join(self.books)

axundov = Library()

axundov + 'Sefiller'
axundov + 'Cinayet ve ceza'

print(axundov)

