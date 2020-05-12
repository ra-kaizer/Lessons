# вариант №1-------------------------------------------
my_line = input("введите строку: ")
my_word = []
my_word = my_line.split()
for ind, el, in enumerate(my_word, 1):
    print(f" {ind} {el[0:10]}")

# вариант №2-------------------------------------------
my_line = input("введите строку: ")
my_word = []
num = 1
for elem in range(my_line.count(' ') + 1):
    my_word = my_line.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[elem]}")
        num += 1
    else:
        print(f" {num} {my_word[elem][0:10]}")
        num += 1