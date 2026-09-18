# Класс — шаблон для создания объектов.
# Car — родительский класс, суперкласс, с общими свойствами и действиями машины.
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


# Bus и ElectricCar — дочерние классы, подклассы, или потомки Car.
# Они наследуют его общие атрибуты и методы.
# Каждый из них переопределяет drive_to и едет по-своему.
class Bus(Car):
    def drive_to(self, destination):
        print(f"Автобус цвета {self.color} поехал: {destination}")


class ElectricCar(Car):
    def drive_to(self, destination):
        print(f"Электро-машина модели {self.model} поехала в/на {destination}")


car_1 = Car("Kia", "серебристый")
tesla_1 = ElectricCar("Tesla", "black")
bus35 = Bus("Mercedes", "green")

# Можно вызвать drive_to у каждого объекта отдельно:
# car_1.drive_to("Кара-Балта")
# tesla_1.drive_to("Кара-Балта")
# bus35.drive_to("Кара-Балта")

# Объекты разных классов можно собрать в одну коллекцию.
vehicles = (car_1, tesla_1, bus35)

# Полиморфизм: один и тот же вызов использует подходящий
# вариант drive_to для каждого конкретного объекта.
for one_vehicle in vehicles:
    one_vehicle.drive_to(destination="Кара-Балта")
