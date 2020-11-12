class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        data = date.split(".")
        year = int(data[2])
        month = cls.numbers_to_months(data[1])
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            rented = "rented"
        else:
            rented = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}"

    @staticmethod
    def numbers_to_months(number: str):
        month = ""
        months = (
            ["01", "January"],
            ["02", "February"],
            ["03", "March"],
            ["04", "April"],
            ["05", "May"],
            ["06", "June"],
            ["07", "July"],
            ["08", "August"],
            ["09", "September"],
            ["10", "October"],
            ["11", "November"],
            ["12", "December"]
        )
        for m in months:
            if number == m[0]:
                month = m[1]
        return month


