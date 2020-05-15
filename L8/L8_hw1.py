class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def conv_to_int(cls, str_val):
        return [val for val in map(int, str_val.split('-'))]

    @staticmethod
    def valid(str_val):
        day, month, year = map(int, str_val.split('-'))
        return day <= 31 and month <= 12 and year <= 3000


today = ('14-05-2020')
print(Date.conv_to_int(today))
print(Date.valid(today))
