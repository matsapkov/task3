import random
from player import Player

player1 = Player(300)
class Field:

    obstacle_probability = [0.1, 0.2, 0.3]
    SIZE = 0
    __game_field = [[]]
    coordinates = {}
    __sub_game_field = [[]]

    def __init__(self, size):
        self.SIZE = size
        self.game_field = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.create_coordinates()

    def fill_field(self, game_field, obstacle_probability):
        for i in range(1, self.SIZE - 1):
            for j in range(self.SIZE):
                rand = random.random()
                if rand < obstacle_probability[0]:
                    self.game_field[i][j] = '^'             #гора
                    self.sub_game_field[i][j] = '^'
                elif rand < obstacle_probability[1]:
                    self.game_field[i][j] = '#'           #болото
                    self.sub_game_field[i][j] = '#'
                elif rand < obstacle_probability[2]:
                    self.game_field[i][j] = '{}'            #холм
                    self.sub_game_field[i][j] = '{}'
                else:
                    self.game_field[i][j] = '*'           #обычная равнина
                    self.sub_game_field[i][j] = '*'

        for j in range(self.SIZE):
            self.game_field[0][j] = '*'
            self.game_field[self.SIZE - 1][j] = '*'
            self.sub_game_field[0][j] = '*'
            self.sub_game_field[self.SIZE - 1][j] = '*'

    def create_coordinates(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(self.SIZE):
            self.coordinates[i] = {}
            for j in range(self.SIZE):
                self.coordinates[i][j] = f'{letters[j]}{i}'
    def print_field(self, game_field):
        for row in game_field:
            print(' '.join(map(str, row)))

    def print_coordinates(self):
        for i in range(self.SIZE):
            for j in range( self.SIZE):
                print(self.coordinates[i][j], end='\t')
            print()

    def spawn_units(self):
        occupied_coordinates = set()
        for unit in player1.get_units():
            unit.Position_i = 0
            while True:
                unit.Position_j = random.randint(0, self.SIZE - 1)
                if unit.Position_j not in occupied_coordinates:
                    occupied_coordinates.add(unit.Position_j)
                    self.game_field[unit.Position_i][unit.Position_j] = player1.get_units.index(unit)
                    break

    @property
    def get_sub_game_field(self):
        return self.sub_game_field

playground = Field(15)
playground.fill_field(playground.game_field,playground.obstacle_probability)
playground.print_field(playground.game_field)
print("\nCoordinates:")
playground.print_coordinates()