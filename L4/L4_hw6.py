#a
from itertools import count

for el in count(int(input('Введите стартовое число цикла: '))):
    print(el)

#b
from itertools import cycle

my_list = ['ABC', 54, None, False]
for el in cycle(my_list):
    print(el)
