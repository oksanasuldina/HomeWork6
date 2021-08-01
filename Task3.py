class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.surname, self.name)

    def get_total_income(self):
        print("Доход с учетом премии: {}".format(sum(self._income.values())))


person = Position('Иван', 'Иванов', 'Инженер', 60000, 10000)
person.get_full_name()
person.get_total_income()
