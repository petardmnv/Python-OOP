from typing import List
from guildsystem.player import Player


class Guild:
    name: str
    players: List

    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        guild_names = [p.name for p in self.players]
        if player_name in guild_names:
            self.players[guild_names.index(player_name)].guild = "Unaffiliated"
            self.players.pop(guild_names.index(player_name))
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_inf = f'Guild: {self.name}' + '\n'
        player_inf = [f"{p.player_info()}" for p in self.players]
        return guild_inf + '\n'.join(player_inf)
