class ExercisePlan:
    _id: int = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        ExercisePlan._id += 1
        self.id = ExercisePlan._id

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'

    @classmethod
    def get_next_id(cls):
        return cls._id + 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, duration=hours*60)

