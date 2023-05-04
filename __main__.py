from controller.find_effectiveness import get_stab, get_weak
from cli import print_pokes, print_Moves, print_Move, input_poke_name, print_welcome, damage_inflict_print, select_move
from controller import find_one_poke, get_effectiveness, get_weak, modifier, damage_to_pokemon

print_welcome()
libro = open("./data/pokemon_data.csv", "r")
pokemonAtacante = input_poke_name("Ingrese el nombre del primer Pokémon: ")
pokemonAtacanteObjeto = find_one_poke(pokemonAtacante, libro)
libro.close()
print_pokes(pokemonAtacanteObjeto)
print_Moves(pokemonAtacanteObjeto.moves)
moveToUse = select_move(pokemonAtacanteObjeto.moves)
print_Move(moveToUse)
print(pokemonAtacanteObjeto) 
pokemonDefensor = input_poke_name("Ingrese el nombre a atacar Pokémon: ")
libro = open("./data/pokemon_data.csv", "r")
pokemonDefensorObjeto = find_one_poke(pokemonDefensor, libro)
pokemonDefensorObjeto.print_pokemon_defensor()
libro.close()
tablaEffectivity = open("./data/tabla_efectividad.csv", "r")
pokeAtacanteBonus, typeOrder = get_effectiveness(tablaEffectivity, moveToUse[2])
pokemonAtacanteBonusVSDefensor = get_weak(pokemonDefensorObjeto.tipo, pokeAtacanteBonus, typeOrder)
pokemonAtacanteStab = get_stab(pokemonAtacanteObjeto, moveToUse[2])
modifierMove = modifier(pokemonAtacanteBonusVSDefensor, pokemonAtacanteStab)
damage = damage_to_pokemon(moveToUse[1], pokemonAtacanteObjeto, pokemonDefensorObjeto, modifierMove, moveToUse[3])
damage_inflict_print(pokemonAtacanteObjeto, pokemonDefensorObjeto, damage)
#By Darthsita
