# создаем класс для склада
class Warehouse:
    def __init__(self):
        # переменная для хранения общего количества товаров
        self.total_qty = 0
        # создаем словарь для хранения всех элементов
        self.unit = {}
        # создадим кортеж с шаблоном запрашиваемых данных
        self.questions_template = (
            {'Наименование': 'Введите наименование товара: '},
            {'Цена': 'Введите цену:  '},
            {'Количество': 'Введите количество: '}
        )

    @staticmethod
    def is_int(number: str):
        """ функция проверяет является ли аргумент целым числом, независимо от знака"""
        try:
            int(number)
            return True
        except ValueError:
            return False

    def reception(self):
        # чтобы как-то ограничить ввод пользователя количеством товаров, введем проверку
        user_input = input('Хотите заполнить товары? Введите "yes", либо введите любой текст для отмены: ')
        # создаем список для хранения итога по подразделению
        user_list = []
        while user_input == 'yes':
            # создадим словарь для хранения ответов на вопросы по товарам
            user_dict = {}
            for quest in self.questions_template:
                key = tuple(quest)[0]
                # запрашиваем данные у пользователя, задавая последовательно вопросы
                tmp = input(quest[key])
                # проверка на целое число, в зависимости от ключа и соответственно преобразование
                if key == 'Цена':
                    if self.is_int(tmp):
                        tmp = int(tmp)
                    else:
                        print('Неверный тип данных! Ввод прерван.')
                        return
                elif key == 'Количество':
                    if self.is_int(tmp):
                        tmp = int(tmp)
                        self.total_qty += tmp
                    else:
                        print('Неверный тип данных! Ввод прерван.')
                        return
                # заполняем словарь (обновляем данные в нем по ключу)
                user_dict.update({key: tmp})
            # заполняем список введенными данными
            user_list.append(user_dict)
            # запрашиваем подразделение
            user_input = input('Введите название подразделения: ')
            # обновляем данные по всему подразделению
            self.unit.update({user_input: user_list})
            # запрашиваем у пользователя требуется ли продолжать
            user_input = input('Продолжаем заполнение ("yes" - продолжить)? ')


# создаем классы для оргтехники, в том числе наследуемые
class OfficeEquipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name: str, price: int, print: str):
        self.print = print
        super().__init__(name, price)


class Scanner(OfficeEquipment):
    def __init__(self, name: str, price: int, scan: str):
        self.scan = scan
        super().__init__(name, price)


class Xerox(OfficeEquipment):
    def __init__(self, name: str, price: int, copy: str):
        self.copy = copy
        super().__init__(name, price)


# создаем экземпляр класса
warehouse = Warehouse()
# вызываем метод заполнения склада
warehouse.reception()
# выведем содержимое склада
print(warehouse.unit)
# выводим данные по общему количеству всех товаров по всем подразделениям
print(warehouse.total_qty)