from models import Poke

def print_pokes(pokemon):    
    statsBase = pokemon.dicctonary()
    print(
    f"""
    ________________________________________________________________________       
    Estadísticas base del pokémon:  
    El HP Base de {statsBase["NAME"]}: {statsBase["HP_base"]}
    El ATK Base de {statsBase["NAME"]} es : {statsBase["ATK"]}
    El DEF Base de {statsBase["NAME"]} es : {statsBase["DEF"]}
    El ATK ESP Base de {statsBase["NAME"]} es : {statsBase["ATKESP"]}
    El DEF ESP Base de {statsBase["NAME"]} es : {statsBase["DEFESP"]}
    El SPE Base de {statsBase["NAME"]} es : {statsBase["VEL"]}
    ________________________________________________________________________
    """)

def print_Moves(moves):
    counter = 0
    print(" Movimientos que puede aprender el pokémon: ")
    for move in moves:
        print(f" {counter}  -  {move} " )
        counter += 1

def print_Move(move):
    print(f"""
    El ataque seleccionado es: {move[0]}
    Poder de ataque es: {move[1]}
    """)

def print_welcome():
    print("Bienvenido al simulador")

def damage_inflict_print(pokemon_object_1, pokemon_object_2, damage):
    print(f"""
    ____________________________________________________________________________________________________________________________
    El daño que realizó {pokemon_object_1.name} a {pokemon_object_2.name} fue de: {damage} 
    
    {pokemon_object_2.name} quedó con un HP de: {pokemon_object_2.hpIVTotal}/{round((pokemon_object_2.hpIVActual - damage), 2)}
    ____________________________________________________________________________________________________________________________
    """)
