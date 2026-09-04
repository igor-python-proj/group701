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
    def __init__(self, model, color, battery):
        super().__init__(model, color)
        self.battery = battery

    def charge(self):
        self.battery += 15
        if self.battery > 100:
            self.battery = 100

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Электро-машина модели {self.model} поехала в/на {destination}")


tesla_1 = ElectricCar("Tesla", "black", 80)
print(tesla_1.model, tesla_1.color, tesla_1.battery, tesla_1.max_speed)
tesla_1.charge()
print(tesla_1.battery)
tesla_1.charge()
print(tesla_1.battery)
tesla_1.drive_to("Иссык-Куль")


bus35 = Bus("Mercedes", "green")
print(bus35, bus35.color, bus35.model)
bus35.drive_to("Джал")
# print(bus35.battery) # нет такого атрибута