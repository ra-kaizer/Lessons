my_list = [300, 1326, 54, 12, 70, 5, 45, 100]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1] if num - 1 >= 0]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
