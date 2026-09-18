class Animal:
    def move(self):
        print("я не знаю кто я, просто двигаюсь")

class Swimming(Animal):
    def move(self):
        print("Плыву")
        super().move()

class Flying(Animal):
    def move(self):
        print("Лечу")
        super().move()

class Duck(Flying, Swimming):
    def move(self):
        print("я утка я летаю и плаваю")
        super().move()

donald_duck = Duck()
donald_duck.move()
print(Duck.mro())