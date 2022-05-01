class Clothes:
    def __init__(self, size, type_clothes):
        self.size = size
        self.type_clothes = type_clothes

    def fabric_calculation(self):
        if self.type_clothes == 'coat':
            number_of_fabric_types = self.size / 6.5 + 0.5
        elif self.type_clothes == 'suit':
            number_of_fabric_types = self.size * 2 + 0.3
        else:
            print('Не верно указанно изделие')
            exit()
        return number_of_fabric_types

if __name__ == '__main__':
    my_coat = Clothes(48, 'coat')
    number_of_fabrics = Clothes.fabric_calculation(my_coat)
    my_suit = Clothes (1.92, 'suit')
    print(f'необходимо ткани {number_of_fabrics} м2')
    number_of_fabrics = Clothes.fabric_calculation(my_suit)
    print(f'необходимо ткани {number_of_fabrics} м2')