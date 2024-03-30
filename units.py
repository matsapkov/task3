from field import Field
import random
class Unit:
    __Name = 'Unit'
    __hit_Points = 0
    __def_Points = 0
    __move_Points = 0
    __attack_Points = 0
    __attack_Range = 0
    __Cost = 0
    Position_i = 0
    Position_j = 0

    def __init__(self, name, hp, dp, mp, ap, ar, cost):
        self.__Name = name
        self.__hit_Points = hp
        self.__def_Points = dp
        self.__move_Points = mp
        self.__attack_Points = ap
        self.__attack_Range = ar
        self.__Cost = cost

    @property
    def get_name(self):
        return self.__Name

    @property
    def get_cost(self):
        return self.__COST

    def moving(self):

    def attack(self):





