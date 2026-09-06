# Класс — шаблон для создания объектов.
# Car — родительский класс, суперкласс: описывает общие свойства и действия машин.
class Car:
    # __init__ — конструктор: Python вызывает его автоматически при Car(...)
    # self — сам конкретный объект; Python передаёт его в метод автоматически
    def __init__(self, model, color):
        # self.model и self.color — атрибуты (данные) конкретного объекта.
        self.model = model
        self.color = color
        self.max_speed = 100

    # Метод — это функция, описанная внутри класса.
    def drive_to(self, destination):
        print(f"Машина цвета '{self.color}', модели {self.model} поехала в/на {destination}")

    def change_color(self, new_color):
        self.color = new_color


# Bus — дочерний класс, подкласс, или потомок Car.
# Он получает атрибуты и методы Car, но переопределяет drive_to.
class Bus(Car):
    def drive_to(self, destination):
        print(f"Автобус цвета {self.color} поехал: {destination}")


# ElectricCar — тоже дочерний класс (подкласс) Car,
# но он добавляет батарею и зарядку.
class ElectricCar(Car):
    def __init__(self, model, color, battery):
        # super().__init__ вызывает конструктор родительского класса Car.
        super().__init__(model, color)
        # battery — дополнительный атрибут электромобиля.
        self.battery = battery

    def charge(self):
        # При каждой зарядке добавляем 15%, но заряд не может быть больше 100%.
        self.battery += 15
        if self.battery > 100:
            self.battery = 100

    def drive_to(self, destination):
        # Сначала выполняем метод родителя, затем добавляем сообщение электромобиля.
        super().drive_to(destination)
        print(f"Электро-машина модели {self.model} поехала в/на {destination}")


# Создаем конкретный объект по шаблону ElectricCar.
tesla_1 = ElectricCar("Tesla", "black", 80)
print(tesla_1.model, tesla_1.color, tesla_1.battery, tesla_1.max_speed)
tesla_1.charge()
print(tesla_1.battery)
tesla_1.charge()
print(tesla_1.battery)
tesla_1.drive_to("Иссык-Куль")


# Bus получил свойства Car, но атрибута battery у него нет.
bus35 = Bus("Mercedes", "green")
print(bus35, bus35.color, bus35.model)
bus35.drive_to("Джал")
# print(bus35.battery)  # Ошибка: battery есть только у ElectricCar.
