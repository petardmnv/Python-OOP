class Subscription:
    _id: int = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        Subscription._id += 1
        self.id = Subscription._id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @classmethod
    def get_next_id(cls):
        return cls._id + 1
