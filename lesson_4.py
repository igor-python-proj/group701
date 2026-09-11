# Абстракция
# Вызывающему коду достаточно знать общее действие send(),
# а детали отправки будут разными у каждого способа уведомления.
from abc import ABC, abstractmethod

# Notification описывает общий интерфейс для всех уведомлений.
class Notification(ABC):
    # @abstractmethod помечает метод, который обязательно должны реализовать наследники.
    @abstractmethod
    def send(self, message):
        # В базовом классе нет конкретного способа отправки сообщения.
        pass

# Конкретные классы реализуют один и тот же метод своим способом.
class EmailNotification(Notification):
    def send(self, message):
        print(f"Уведомление по почте: {message}")

class TelegramNotification(Notification):
    def send(self, message):
        print(f"Телеграм уведомление: {message}")

# Этот класс не реализовал обязательный метод send().
class IncompleteNotification(Notification):
    pass

# Абстрактный класс и его неполного наследника создать нельзя.
# not1 = Notification() # ошибка
# Эти классы реализовали send(), поэтому их объекты создавать можно.
not2 = EmailNotification()
not3 = TelegramNotification()
not2.send("У вас закончился баланс")
not3.send("У вас закончился баланс")

# При создании IncompleteNotification Python обнаруживает нереализованный метод.
try:
    not4 = IncompleteNotification()
except TypeError:
    print("Нельзя инициализировать класс с нереализованным send")
