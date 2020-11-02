import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = list()

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
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
            f"Pokemon Trainer {self.name}'"
            f"Pokemon count {len(self.pokemon)}"
        ]
        pokemon_datails = [f'- {p.pokemon_details()}' for p in self.pokemon]
        return '\n'.join(trainer_details + pokemon_datails)
