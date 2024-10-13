from typing import List, Tuple
from pokemon import pokemon
from poketype import poketype

class aquapokemon(pokemon):
    def __init__(self, name, pokeId, level, living_points, attacking_points, defence_points, attack):
        super().__init__(name, pokeId, level, living_points, attacking_points, defence_points, attack)

        self.type : poketype = poketype(0)

    def lvlup(self) -> pokemon:
        pass