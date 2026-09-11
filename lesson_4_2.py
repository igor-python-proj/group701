# переменные класса и виды методов
# Атрибуты класса принадлежат самому классу и являются общими для его объектов.

class Visitor:
    # Переменные класса: одна организация и один общий счётчик посетителей.
    organisation = "Geeks"
    count = 0

    def __init__(self, name):
        # Проверяем имя до сохранения его в объекте.
        if not self.validate_name(name):
            raise ValueError("Имя не должно быть пустым")
        self.name = name
        # Увеличиваем именно общий счётчик класса.
        # self.count = 0 - не работает так как об-ы не умеют получать доступ к другим об-м
        Visitor.count += 1

    @classmethod
    def get_visitor_count(cls):
        # cls — это класс, через который вызвали метод; self здесь не нужен.
        return cls.count

    @classmethod
    def from_text(cls, text):
        # Альтернативный конструктор подготавливает текст перед созданием объекта.
        text = text.strip()
        new_visitor = Visitor(text)
        return new_visitor

    @staticmethod
    def validate_name(name):
        # Статический метод не получает автоматически ни self, ни cls.
        if name.strip():
            return True
        return False


# Создание каждого объекта увеличивает общий Visitor.count.
visitor1 = Visitor("Игорь")
visitor2 = Visitor("Алмаз")
# Изменение атрибута класса видно всем объектам, если объект не создал своё значение.
Visitor.organisation = "Об.Ц. Geeks"
print(Visitor.organisation, Visitor.count)
print(Visitor.get_visitor_count())
print(Visitor.validate_name("       "))
# from_text() удаляет пробелы и создаёт посетителя с очищенным именем.
visitor3 = Visitor.from_text("        Мурат      ")
print(visitor3.name, Visitor.get_visitor_count())
# После strip() остаётся пустая строка, поэтому создаётся ValueError.
visitor3 = Visitor.from_text("           ")
