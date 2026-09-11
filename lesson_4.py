# Абстракция
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Уведомление по почте: {message}")

class TelegramNotification(Notification):
    def send(self, message):
        print(f"Телеграм уведомление: {message}")

class IncompleteNotification(Notification):
    pass

# not1 = Notification() # ошибка
not2 = EmailNotification()
not3 = TelegramNotification()
not2.send("У вас закончился баланс")
not3.send("У вас закончился баланс")

try:
    not4 = IncompleteNotification()
except TypeError:
    print("Нельзя инициализировать класс с нереализованным send")