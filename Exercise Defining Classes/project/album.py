from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = []
        for i in args:
            if not i.single:
                self.songs.append(i)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if song.name in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        if song_name in [s for s in self.songs]:
            song_to_be_removed = [s for s in self.songs if s == song_name]
            self.songs.remove(song_to_be_removed)
            return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = ""
        result += f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"

        return result


song = Song("Running in the 90s", 3.45, False)

print(song.get_info())

album = Album("Initial D", song)

second_song = Song("Around the World", 2.34, False)

print(album.add_song(second_song))

print(album.details())

print(album.publish())

