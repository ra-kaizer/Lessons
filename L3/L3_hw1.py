def degree(a, b):
    try:
        deg = float(a) / float(b)
        return round(deg, 2)
    except (ValueError, TypeError):
        print('Ошибка!!! Введите число!')
    except ZeroDivisionError:
        print("число 'b' не может быть числом ноль")


print(degree(input("Введите число 'a': "), (input("Введите число 'b': "))))
