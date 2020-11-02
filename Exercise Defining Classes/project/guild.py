from  typing import List
from project.player import Player
class Guild:
    name: str
    players: List

    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player: Player):
        pass

    def kick_player(self, player_name: str):
        pass

    def guild_info(self):
        pass

