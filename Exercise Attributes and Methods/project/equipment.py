class Equipment:
    _id: int = 0

    def __init__(self, name: str):
        self.name = name
        Equipment._id +=1
        self.id = Equipment._id

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'

    @staticmethod
    def get_next_id(cls):
        return cls._id + 1


