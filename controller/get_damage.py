import random as rnd

def modifier(pokemon_type_bonus, stab):
    return float(pokemon_type_bonus) * stab * rnd.uniform(0.85,1.0)*1

def damage_to_pokemon(power, pokemon_object_1, pokemon_object_2, modifier, category):
    if (category == "physical"):
        return round((((((2*50/5)+ 2)*float(power)*(float(pokemon_object_1.atkIV)/float(pokemon_object_2.defIV)))/50)+2)*float(modifier), 2)
    if (category == "special"):
        return round((((((2*50/5)+ 2)*float(power)*(float(pokemon_object_1.atkespIV)/float(pokemon_object_2.defespIV)))/50)+2)*float(modifier), 2)