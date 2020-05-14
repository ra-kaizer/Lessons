import traceback


class My_Exception(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class Check_n_add:

    def __init__(self):
        self.__result = []
        while True:
            data = input('Введите положительное число: ')
            if data == 'stop':
                break
            try:
                self.__result.append(int(data))
            except ValueError:
                print('Вы ввели не число!!!\n\n', traceback.format_exc())
            except Exception:
                raise My_Exception('Какая-то другая ошибка')

    def __str__(self):
        return ', '.join(map(str, self.__result))


if __name__ == '__main__':
    c = Check_n_add()
    print(c)
