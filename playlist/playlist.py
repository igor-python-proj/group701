# Магические методы, dunder методы

class Playlist:
    def __init__(self, name, tracks):
        self.name = name
        self.__tracks = tracks

    def __len__(self):
        return len(self.__tracks)

    def __str__(self):
        return f"Плейлист  {self.name}, {len(self.__tracks)} треков"

    def __getitem__(self, item):
        if item < 0 or item >= len(self.__tracks):
            raise IndexError("В вашем плейлисте нет песен по такому индексу")
        return self.__tracks[item]

playlist = Playlist("favourite songs", ["Espresso", "Good Luck, Babe!"])
l = len(playlist)
print(l)
print(playlist)
print(playlist[1])
try:
    print(playlist[100])
except IndexError as e:
    print(e)

print("Espresso" in playlist)

