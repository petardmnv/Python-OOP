from project.user import User
from  typing import Dict, List, ClassVar


class Library:
    user_records = List[User]
    books_available = Dict[str, List[str]]
    rented_books = Dict[str, Dict[str, int]]

    def add_user(self, user: User):
        users = [u.user_id for u in Library.user_records]
        if user.user_id in users:
            return f"User with id = {user.user_id} already registered in the library!"
        Library.user_records.append(user)

    def remove_user(self, user: User):
        users = [u.user_id for u in Library.user_records]
        if user.user_id not in users:
            return "We could not find such user to remove!"
        Library.user_records.pop(users.index(user.user_id))

    def change_username(self, user_id: int, new_username: str):
        users = [u.user_id for u in Library.user_records]
        if user_id in users:
            if new_username == Library.user_records[users.index(user_id)].username:
                return "Please check again the provided username - it should be different than the username used so " \
                       "far! "
            Library.user_records[users.index(user_id)].username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"


user = User(1, "Peter")
user1 = User(2, "deter")
library = Library()
library.add_user(user)
library.add_user(user1)
library.remove_user(user1)
print(library.change_username(1, "Peter"))

print(library.change_username(1, "Peho"))
[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]