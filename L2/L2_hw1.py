list_class = [24, None, {-15, 45 / 12}, 'python', False, 12.5, -12, (5, 'program', 1 + 3j), {1: 'value', 'key': 2},
              [1, 2, 3]]


def my_type(element):
    for element in range(len(list_class)):
        print(type(list_class[element]))
    return


my_type(list_class)