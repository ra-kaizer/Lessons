my_list = [1, 5, 8, 6, 2, 1, 5, 12, 8, 1, 7]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)