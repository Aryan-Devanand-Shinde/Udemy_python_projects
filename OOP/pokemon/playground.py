from pokemon import pokemon
from aquapokemon import aquapokemon
from poketype import poketype

squirtle = aquapokemon('squirtle','802',10,10,10,10,[('tackle',5)])

print(squirtle.type.name)

aqua = poketype(0)
fire = poketype(1)
grass = poketype(2)

print(aqua.value < fire.value)