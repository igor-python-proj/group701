# множ наследование
class Flying:
    def fly(self):
        print("Лечу")


class Swimming:
    def swim(self):
        print("Плыву")


class Duck(Flying, Swimming):
    pass

donald = Duck()
donald.fly()
donald.swim()
