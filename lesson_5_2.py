# Миксин — небольшой класс, который добавляет готовое поведение другим классам.
class InfoMixin:
    # Для работы show_info() объект должен предоставить метод get_info().
    def show_info(self):
        print(self.get_info())


# NamedObject хранит общую для разных объектов информацию — имя.
class NamedObject:
    def __init__(self, name):
        self.name = name

# Product получает хранение имени от NamedObject и show_info() от InfoMixin.
class Product(InfoMixin, NamedObject):
    def get_info(self):
        return f"Товар: {self.name}"

# Room использует то же поведение миксина, но формирует свой текст.
class Room(InfoMixin, NamedObject):
    def get_info(self):
        return f"Помещение: {self.name}"

# show_info() общий, а get_info() вызывается из конкретного класса.
Product("Хлеб").show_info()
Room("Аудитория 4/3").show_info()

