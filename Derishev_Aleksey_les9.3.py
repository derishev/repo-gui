class Worker:

    def __init__(self, name, surname, position, income):
        self.income = {"wage": 0, "bonus": 0}
        self.name = name
        self.surname = surname
        self.position = position
        self.income['wage'] = income
        self.income['bonus'] = income * 0.1

class Position(Worker):
    def get_full_name(self):
        print(fr'Имя работника {self.name} {self.surname}')

    def get_total_income(self):
        full_income = self.income['wage'] + self.income['bonus']
        print(fr'Полная зарплата {full_income} рублей')

if __name__ == '__main__':
    my_person = Position('Nikola', 'Ivanov', 'Direktor', 1500)
    my_person.get_full_name()
    my_person.get_total_income()