# Инкапсуляция — хранение важных данных внутри класса
# и изменение этих данных через методы с проверками.
class BankAccount:
    def __init__(self, owner, identity, name):
        # Одинарное подчёркивание обозначает protected-атрибут — договорённость:
        # такой атрибут не следует менять напрямую снаружи.
        self._owner = owner
        # Два подчёркивания обозначают private-атрибуты:
        # Python скрывает их обычное имя, поэтому напрямую снаружи к ним не обращаются.
        self.__identity = identity
        self.__balance = 0
        self.__name = ""
        self.name = name

    def __test_private(self):
        print(self.__name)

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

    # геттер ....
    def get_name(self):
        return self.__name

    # Сеттер — метод, через который изменяем значение приватного атрибута с проверкой.
    def set_name(self, new_name):
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Имя счета не должно быть пустым")
        self.__name = new_name

    # геттер
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Имя счета не должно быть пустым")
        self.__name = new_name

igor_account = BankAccount("Igor", "fjdsjgof", "Основной")
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

print(igor_account.get_name())
igor_account.set_name("Зарплата")
print(igor_account.name)
igor_account.name = "Зарплата другая"
print(igor_account.name)
igor_account._owner = "Nikolay"  # технически можно, но так нарушается договоренность.