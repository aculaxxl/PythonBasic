class Book:
    def __init__(self, title: str, author: str, is_avaible: bool):
        self.title = title
        self.author = author
        self.is_avaible = is_avaible

    def borrow(self):
        self.is_avaible = False
    
    def return_book(self):
        self.is_avaible = True
    def __str__(self):
        return f'{self.title} - {self.author}'

class User:
    def __init__(self, name: str, borrowed_books = []):
        self.name = name
        self.borrowed_books = []
    def __str__(self):
        return self.name
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.borrow()
    def return_book(self,book):
        self.borrowed_books.remove(book)
        book.return_book()
   

    


class Library:
    def __init__(self, books = None,  users = None):
        self.books = books or []
        self.users = users or []
    def add_book(self, book):
        self.books.append(book)
    def add_user(self, user):
        self.users.append(user)
    def get_book_list(self):
        return self.books
    def get_users_list(self):
        return self.users
    def lend_book(self, user, book):
        for u in self.users:
            if user.name == u.name:
                user = u
                for b in self.books:
                    if book.title == b.title:
                        book = b
                        user.borrow_book(book)

book1 = Book("Майстер і Маргарита", 'Булгаков', True)
book2 = Book('Гаррі Поттер', 'Джоан Роулінг', False)

user1 = User('Ірина')
user2 = User('Єлизавета')
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)


library.lend_book(user2, book1)
for book in user2.borrowed_books:
    print("user2 borrowed books is:" , book)
for book in library.books:
    print(book, book.is_avaible)

