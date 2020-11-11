import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages=math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for ind, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {ind + 1} slot {len(page)}"
        return "No more free spots"

    def display(self):
        res = []
        for p in self.photos:
            res.append('-' * 11)
            res.append(('[] ' * len(p)).rstrip(' '))
        res.append('-' * 11)
        return '\n'.join(res) + '\n'


album = PhotoAlbum.from_photos_count(7)
print(album.pages)


print(album.add_photo("baby"))

print(album.add_photo("first grade"))

print(album.add_photo("eight grade"))

print(album.add_photo("party with friends"))

print(album.photos)

print(album.add_photo("prom"))

print(album.add_photo("wedding"))

print(album.photos)
print(album.display())
