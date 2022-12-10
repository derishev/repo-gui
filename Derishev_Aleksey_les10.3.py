class Cell:
    def __init__(self, number_cell):
        self.number_cell = number_cell

    def __add__(self, other):
        return self.number_cell + other.number_cell

    def __sub__(self, other):
        if self.number_cell < other.number_cell:
            print('Нельзя выполнить это действие')
            exit()
        return self.number_cell - other.number_cell

    def __mul__(self, other):
        return self.number_cell * other.number_cell

    def __truediv__(self, other):
        return self.number_cell // other.number_cell

    def make_order(self, argument):
        a_stroka = ''
        a = self.number_cell // argument
        b = self.number_cell % argument
        for i in range(a):
            a_stroka = a_stroka + '*' * argument + r'\n'
        a_stroka = a_stroka + '*' * b

        return a_stroka



my1_cell = Cell(19)
my2_cell = Cell(12)
print(my1_cell + my2_cell)
print(my1_cell - my2_cell)
print(my1_cell * my2_cell)
print(my1_cell / my2_cell)
print(my1_cell.make_order(5))