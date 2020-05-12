goods = int(input("Введите количество товара: "))
n = 1
my_list = []
while n <= goods:
    my_dict = dict({'товар': input("Введите название товара: "), 'цена товара': input("Введите цену товара: "),
                    'количество товара': input('Введите количество товаров: '),
                    'единица измерения': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1
for el in my_list:
    print(el)