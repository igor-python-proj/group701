# переменные класса и виды методов

class Visitor:
    # переменные класса
    organisation = "Geeks"
    count = 0

    def __init__(self, name):
        if not self.validate_name(name):
            raise ValueError("Имя не должно быть пустым")
        self.name = name
        # self.count = 0 - не работает так как об-ы не умеют получать доступ к другим об-м
        Visitor.count += 1

    @classmethod
    def get_visitor_count(cls):
        return cls.count

    @classmethod
    def from_text(cls, text):
        text = text.strip()
        new_visitor = Visitor(text)
        return new_visitor

    @staticmethod
    def validate_name(name):
        if name.strip():
            return True
        return False


visitor1 = Visitor("Игорь")
visitor2 = Visitor("Алмаз")
Visitor.organisation = "Об.Ц. Geeks"
print(Visitor.organisation, Visitor.count)
print(Visitor.get_visitor_count())
print(Visitor.validate_name("       "))
visitor3 = Visitor.from_text("        Мурат      ")
print(visitor3.name, Visitor.get_visitor_count())
visitor3 = Visitor.from_text("           ")