from spoopify.album import Album, Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = list()

    def add_album(self, album: Album):
        if album.name in [i.name for i in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_names = [i.name for i in self.albums]
        if album_name in album_names:
            if self.albums[album_names.index(album_name)].published:
                return "Album has been published. It cannot be removed."
            del self.albums[album_names.index(album_name)]
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        res = ""
        res += f"Band {self.name}\n"
        for a in self.albums:
            res += a.details()
        return res

