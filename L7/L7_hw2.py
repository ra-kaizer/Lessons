class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_c(self):
        return round((self.size / 6.5 + 0.5), 2)

    def get_square_j(self):
        return round((self.height * 2 + 0.3), 2)

    @property
    def get_sq_full(self):
        return str(f'(общая площадь ткани) \n'
                   f' {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):
        return f'Необходимая площадь ткани на пальто {self.get_square_c()}'


class Jacket(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):
        return f'Необходимая площадь ткани на костюм {self.get_square_j()}'


coat = Coat(45, 168)
jacket = Jacket(96, 168)

print(coat)
print(jacket)

print("\n для пальто", coat.get_sq_full)
print("для костюма", jacket.get_sq_full)

# проверка ответа
print("\n", coat.get_square_c())
print(jacket.get_square_j())
