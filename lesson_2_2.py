# родительский класс, суперкласс
class Car:
    # __init__ — конструктор: Python вызывает его автоматически при Car(...)
    # self — конкретный создаваемый объект
    def __init__(self, model, color):
        # self.model и self.color — атрибуты объекта
        self.model = model
        self.color = color
        self.max_speed = 100

    def drive_to(self, destination):
        print(f"Машина цвета '{self.color}', модели {self.model} поехала в/на {destination}")

    def change_color(self, new_color):
        self.color = new_color


# Дочерние классы, подклассы, потомки класса 'Car'
class Bus(Car):
    def drive_to(self, destination):
        print(f"Автобус цвета {self.color} поехал: {destination}")


class ElectricCar(Car):
    def drive_to(self, destination):
        print(f"Электро-машина модели {self.model} поехала в/на {destination}")


car_1 = Car("Kia", "серебристый")
tesla_1 = ElectricCar("Tesla", "black")
bus35 = Bus("Mercedes", "green")
# car_1.drive_to("Кара-Балта")
# tesla_1.drive_to("Кара-Балта")
# bus35.drive_to("Кара-Балта")
vehicles = (car_1, tesla_1, bus35)
for one_vehicle in vehicles:
    one_vehicle.drive_to(destination="Кара-Балта")
