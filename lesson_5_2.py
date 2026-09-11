class InfoMixin:
    def show_info(self):
        print(self.get_info())

class NamedObject:
    def __init__(self, name):
        self.name = name

class Product(InfoMixin, NamedObject):
    def get_info(self):
        return f"Товар: {self.name}"

class Room(InfoMixin, NamedObject):
    def get_info(self):
        return f"Помещение: {self.name}"

Product("Хлеб").show_info()
Room("Аудитория 4/3").show_info()

