# Инкапсуляция — хранение важных данных внутри класса
# и изменение этих данных через методы с проверками.
class BankAccount:
    def __init__(self, owner, identity):
        # Одинарное подчёркивание обозначает protected-атрибут — договорённость:
        # такой атрибут не следует менять напрямую снаружи.
        self._owner = owner
        # Два подчёркивания обозначают private-атрибуты:
        # Python скрывает их обычное имя, поэтому напрямую снаружи к ним не обращаются.
        self.__identity = identity
        self.__balance = 0

    def deposit(self, amount):
        # Пополняем счет только положительной суммой.
        if amount > 0:
            self.__balance += amount
        else:
            # ValueError — исключение для неподходящего значения;
            # raise сообщает об ошибке и прерывает выполнение метода.
            raise ValueError("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        # Перед снятием проверяем сумму и наличие денег на счете.
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        elif amount > self.__balance:
            raise ValueError("Недостаточно средств")
        else:
            self.__balance -= amount

    # Геттер — метод, через который получаем значение приватного атрибута.
    def get_balance(self):
        return self.__balance

    # Сеттер — метод, через который изменяем значение приватного атрибута с проверкой.
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount


igor_account = BankAccount("Igor", "fjdsjgof")
# Такое присваивание создало бы обычный balance и не изменило бы __balance.
# igor_account.balance = 1_000_000
print(igor_account.get_balance())
igor_account.deposit(100)
print(igor_account.get_balance())

# Ошибка от неправильного пополнения перехватывается, поэтому программа продолжается.
try:
    igor_account.deposit(-1000)
except ValueError as e:
    print(e)

print(igor_account.get_balance())
igor_account.withdraw(50)
print(igor_account.get_balance())

# Денег недостаточно, поэтому withdraw вызывает ValueError.
# try/except ловит ошибку, и программа продолжает работу.
try:
    igor_account.withdraw(500)
except ValueError as e:
    print(e)

print(igor_account.get_balance())
igor_account.set_balance(100)
igor_account._owner = "Nikolay"  # технически можно, но так нарушается договоренность.

