class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        if self.number_of_floors < 1:
            return 0
        else:
            return self.number_of_floors

    def __str__(self):
        if self.name:
            return f'Название {self.name} кол-во этажей {self.number_of_floors}'
        else:
            return 'Неизвестный дом'

    def go_to(self, new_floor):
        if new_floor >= self.number_of_floors or new_floor < 1:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')


h1 = House('"ЖК Эльбрус"', 10)
h2 = House('"ЖК Акация"', 20)
h1.go_to(5)
h2.go_to(10)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
