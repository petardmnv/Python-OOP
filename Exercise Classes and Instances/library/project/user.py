#from project.library import Library


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: 'Library'):
        if book_name in library.books_available[author]:
            library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            names = [n.username for n in library.user_records]
            for n in names:
                if book_name in library.rented_books[n]:
                    return f"The book {book_name} is already rented and will be available in " \
                           f"{library.rented_books[n][book_name]} days! "

    def return_book(self, author: str, book_name: str, library: 'Library'):
        if book_name in self.books:
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


