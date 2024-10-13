from pokemon import pokemon
from poketype import poketype

class firepokemon(pokemon):
    def __init__(self, name, pokeId, level, living_points, attacking_points, defence_points, attack):
        super().__init__(name, pokeId, level, living_points, attacking_points, defence_points, attack)

        self.type : poketype = poketype(1)    