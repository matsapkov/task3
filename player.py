from units import Unit

Swordsman = Unit('Swordsman', 50, 8,3, 5,1, 10, 0,0)
Horseman = Unit('Horseman', 30, 7, 6,5,1,20,0,0)
Archer = Unit('Archer', 30,8,2,6,5,15,0,0)
class Player:
    __BALANCE = 0
    __units = []

    def __init__(self, balance):
        self.BALANCE = balance

    def unit_to_buy(self):
        self.__unit_type = input("Введите тип юнита для покупки (Swordsman, Horseman, Archer): ")
        return self.__unit_type

    def buy_units(self):
        if (self.__unit_to_buy() == Swordsman.get_name() and self.BALANCE >= Swordsman.get_cost()):
            self.__units.append(Swordsman)
            self.BALANCE -= Swordsman.get_cost()
        elif (self.__unit_to_buy() == Archer.get_name() and self.BALANCE >= Archer.get_cost()):
            self.__units.append(Archer)
            self.BALANCE -= Archer.get_cost()
        elif (self.__unit_to_buy() == Horseman.get_name() and self.BALANCE >= Horseman.get_cost()):
            self.__units.append(Horseman)
            self.BALANCE -= Horseman.get_cost()
        else:
            print("Денег нет, но вы держитесь там, всего хорошего Вам")

    @property
    def get_units(self):
        return self.__units

    def display_units(self):
        for i, unit in enumerate(self.__units):
            print("Номер юнита на поле", i, "Тип юнита", unit)
