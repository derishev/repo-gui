class Matrix:
    def __init__(self, *args):
        self.my_list = args[ :]

    def __str__(self):
        for i in self.my_list:
            i_str = str(i)
            print(i_str)
        return ''

    def __add__(self, other):
        for i_str in range(len(self.my_list)):
            for i_column in range(len(self.my_list[i_str])):
                self.my_list[i_str][i_column] = self.my_list[i_str][i_column] + other.my_list[i_str][i_column]
        return Matrix.__str__(self)



a = Matrix([1, 123, 456], [2, 999, 789], [3, 897, 888])
b = Matrix([322, 890, 1], [321, 98, 876], [6, 5, 9])
c = a + b
print(a)
