class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income["wage"]
        self._income_bonus = income["bonus"]

class Position(Worker):

    def get_full_name(self):
        print(f'Позиция: {self.position} Имя: {self.name} Фамилия: {self.surname}')

    def get_total_income(self):
        print(f'Доход с учётом премии: {self._income_wage + self._income_bonus}')

info = Position('Алексей', 'Смирнов', 'Инженер', {"wage": 30000, "bonus": 2000})
info.get_full_name()
info.get_total_income()