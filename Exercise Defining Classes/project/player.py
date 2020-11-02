from typing import Dict

class Player:
    name: str
    hp: int
    mp: int
    skills: Dict
    guilt: str

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.guild = "Unaffiliated"
        self.skills = dict()

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return 'Skill already added'

    def player_info(self):
        res = ""
        res += f"Name: {self.name}\n"
        res += f"Guilt: {self.guild}\n"
        res += f"HP: {self.hp}\n"
        res += f"MP: {self.mp}\n"
        for s in self.skills:
            res += f"==={s} - {self.skills[s]}\n"
        return res


player = Player("George", 50, 100)

print(player.add_skill("Shield Break", 20))

print(player.player_info())