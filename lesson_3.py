class BankAccount:
    def __init__(self, owner, identity):
        self._owner = owner
        self.__identity = identity
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Вы пытаетесь вложить отрицательное значение")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Вы пытаетесь снять отрицательное значение")
        elif amount > self.__balance:
            raise ValueError("Слишком многого хочешь")
        else:
            self.__balance -= amount

    # геттер - через него получаем значение приватного атрибута
    def get_balance(self):
        return self.__balance

    # сеттер - установить значение приватному атрибуту
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount

igor_account = BankAccount("Igor", "fjdsjgof")
# igor_account.balance = 1_000_000 # обманчивый код
print(igor_account.get_balance())
igor_account.deposit(100)
print(igor_account.get_balance())
try:
    igor_account.deposit(-1000)
except ValueError as e:
    print(e)

print(igor_account.get_balance())
igor_account.withdraw(50)
print(igor_account.get_balance())
igor_account.withdraw(500)
print(igor_account.get_balance())
igor_account.set_balance(100)
igor_account._owner = "Nikolay" # так можно, но не следует

