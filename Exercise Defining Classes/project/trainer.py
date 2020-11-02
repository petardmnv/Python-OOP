from typing import List
from project.pokemon import Pokemon


class Trainer:
    name: str
    pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = list()

    def add_pokemon(self, pokemon: Pokemon):
        p_n = [p.name for p in self.pokemon]
        if pokemon.name not in p_n:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "The pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name in pokemon_names:
            self.pokemon.pop(pokemon_names.index(pokemon_name))
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        trainer_details = [
            f"Pokemon Trainer {self.name}",
            f"Pokemon count {len(self.pokemon)}"
        ]
        pokemon_d = [f'- {p.pokemon_details()}' for p in self.pokemon]
        return '\n'.join(trainer_details + pokemon_d) + '\n'


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.release_pokemon("Pikachu"))
print(trainer.add_pokemon(second_pokemon))
print(trainer.trainer_data())



