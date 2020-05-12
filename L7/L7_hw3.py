class Living_cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        result_add = self.cells + other.cells  #return Living_cell(self.cells + other.cells)
        return Living_cell(result_add)

    def __sub__(self, other):
        if self.cells <= other.cells:
            print('Вычитание невозможно, клетки живые!!!')
            raise ValueError
        result_sub = self.cells - other.cells
        return Living_cell(result_sub)

    def __mul__(self, other):
        result_mul = self.cells * other.cells
        return Living_cell(result_mul)

    def __truediv__(self, other):
        result_truediv = round(self.cells / other.cells)
        return Living_cell(result_truediv)

    def make_order(self, line):
        ordered = ['*' * line for _ in range(self.cells // line)]
        ordered.append('*' * (self.cells % line))
        return f'\n'.join(ordered)

if __name__ == '__main__':

    c1 = Living_cell(10)
    c2 = Living_cell(5)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c1 / c2
    c6 = c1 * c2

    print("\033[31m{}".format(c3))
    print("\033[34m{}".format(c4))
    print("\033[33m{}".format(c5))
    print("\033[32m{}".format(c6))



print(f'c1: cells({c1.cells})\n{c1.make_order(5)}')#ячейка 1
print(f'c2: cells({c2.cells})\n{c2.make_order(5)}')#ячейка 2
print(f'c3: cells({c3.cells})\n{c3.make_order(5)}')#ячейка 1+1
print(f'c4: cells({c4.cells})\n{c4.make_order(2)}')#ячейка 1-1
print(f'c5: cells({c5.cells})\n{c5.make_order(1)}')#ячейка 1/1
print(f'c6: cells({c6.cells})\n{c6.make_order(10)}')#ячейка 1*1
