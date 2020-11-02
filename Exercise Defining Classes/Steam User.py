class SteamUser:
    def __init__(self, username: str, games: list):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game: str, hours: int):
        if game in self.games:
            self.played_hours += abs(hours)
            return f'{self.username} is playing {game}'
        return f'{game} not in library'

    def buy_game(self, game: str):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        return f'{game} is already in your library'

    def stats(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("cs:go", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("C:GO"))
print(user.buy_game("CS:O"))
print(user.buy_game("C:O"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 634))
print(user.stats())
