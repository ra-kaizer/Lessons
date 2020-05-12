def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and b < c:
        return a + c
    else:
        return b + c


print(f'Сумма: {my_func(int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: ")))}')
