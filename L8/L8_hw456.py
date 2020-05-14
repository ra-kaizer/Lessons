class Storage:  # класс склад
    def __init__(self, name, price, amount,title):
        self.name = name
        self.price = price
        self.amount = amount
        self.title = title

    def __str__(self):
        self.title = f'на складе: {self.name} {self.price} {self.amount}'
        return self.title


class Office_eq(Storage):  # класс оргтехника
    def __init__(self, name, price, amount, title):
        super().__init__(name, price, amount, title)
    while True:
        name = input(f'Введите наименование: ')
        price = int(input(f'Введите цену за единицу: '))
        amount = int(input(f'Введите количество: '))
        if input == 'stop':
            break
        try:
            print(f'Текущий список -\n {self.title}') #это не понятно вообще
        except():
            print('Ошибка ввода данных')

class Printer(Storage):
    def to_print(self):
        pass


class Scanner(Storage):
    def to_scan(self):
        pass


class Copier(Storage):
    def to_copier(self):
        pass

unit_1 = Printer('printer', 1000, 1)
unit_2 = Scanner('scanner', 2000, 2)
unit_3 = Copier('copier', 3000, 3)
print(unit_1)
