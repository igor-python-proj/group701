# множ наследование
# Множественное наследование позволяет одному классу получить возможности
# сразу от нескольких родительских классов.
class Flying:
    def fly(self):
        print("Лечу")


class Swimming:
    def swim(self):
        print("Плыву")


# Duck получает метод fly() от Flying, а swim() — от Swimming.
# pass оставляет класс без собственных методов, но наследование сохраняется.
class Duck(Flying, Swimming):
    pass

# Поэтому объект Duck умеет выполнять методы обоих родителей.
donald = Duck()
donald.fly()
donald.swim()
