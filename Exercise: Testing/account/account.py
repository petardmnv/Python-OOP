from typing import List


class Account:
    owner: str
    amount: int
    _transactions: List[int]

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index: int):
        return self._transactions[index]

    def __gt__(self, other: 'Account'):
        return self.balance > other.balance

    def __ge__(self, other: 'Account'):
        return self.balance >= other.balance

    def __lt__(self, other: 'Account'):
        return self.balance < other.balance

    def __le__(self, other: 'Account'):
        return self.balance <= other.balance

    def __eq__(self, other: 'Account'):
        return self.balance == other.balance

    def __ne__(self, other: 'Account'):
        return self.balance != other.balance

    def __add__(self, other: 'Account'):
        new_acc = Account(self.owner + '&' + other.owner, amount=self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc
