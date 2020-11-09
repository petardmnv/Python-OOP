from project.library import Library


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        if book_name == library.books_available[author]:
            if book_name in library.rented_books[self.username]:
                return f"The book {book_name} is already rented and will be available in"\
                        f"{library.rented_books[self.username][book_name]} days! "
            self.books.append(book_name)
            library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library: Library):
        pass

    def info(self):
        pass


user = User(1, "Peter")
user1 = User(2, "deter")
library = Library()
library.add_user(user)
library.add_user(user1)
library.remove_user(user1)
print(library.change_username(1, "Peter"))

print(library.change_username(1, "Peho"))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
