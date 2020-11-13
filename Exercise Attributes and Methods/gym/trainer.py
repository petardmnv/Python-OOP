class Trainer:
    _id: int = 0

    def __init__(self, name: str):
        self.name = name
        Trainer._id += 1
        self.id = Trainer._id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls):
        return cls._id + 1

