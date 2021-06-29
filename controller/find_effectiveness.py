def get_effectiveness(tabla_effectivity, poke_type_move):
    header = tabla_effectivity.readline()
    header = header.strip().split(",")
    for str_row in tabla_effectivity:
        list_row = str_row.strip().split(",")
        if (list_row[0] == poke_type_move):
            poke_effectiveness_type = list_row
    return poke_effectiveness_type, header

def get_weak(poke_type_defender, poke_effectiveness_type_move, typeOrder):
    counter = 1
    while (counter < len(typeOrder)):
        if (poke_type_defender == typeOrder[counter]):
            type_bonus = poke_effectiveness_type_move[counter]
            return type_bonus
        counter += 1

def get_stab(pokemon_object, move_type):
    stab = 1
    if (pokemon_object.tipo == move_type):
        stab = 1.2
    return stab