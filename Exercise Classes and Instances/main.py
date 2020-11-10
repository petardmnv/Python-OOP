from library.project.user import User
from library.project.library import Library

user = User(1, "Peter")
user1 = User(2, "deter")
library = Library()
library.add_user(user)
library.add_user(user1)
library.remove_user(user1)
print(library.change_username(1, "Peter"))

print(library.change_username(1, "Peho"))
[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',

                                                'The Prisoner of Azkaban',

                                                'The Goblet of Fire',

                                                'The Order of the Phoenix',

                                                'The Half-Blood Prince',

                                                'The Deathly Hallows']})

user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)

print(library.books_available)

print(library.rented_books)

print(user.books)

print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))

print(user.return_book('J.K.Rowling', 'The Cursed Child', library))

print(user.return_book('J.K.Rowling', 'The Deathly Hallows', library))

print(library.books_available)

print(library.rented_books)

print(user.books)
