import traceback


class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


if __name__ == '__main__':
    def incorrect(a, b):
        if b == 0:
            raise MyZeroDivision('Нельзя делить на ноль, даже если очень хочется!')
        else:
            return a / b


    try:
        res = incorrect(5, 1)   # или 5, 0
    except MyZeroDivision:
        print('Ошибка деления:\n', traceback.format_exc())
    else:
        print(f'результат деления: {res}')
    finally:
        print('Конец!')

# print(MyZeroDivision)
