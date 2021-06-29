from utils import get_move

def input_poke_name(input_message):
    pokemon = str(input(input_message))
    print(f"Nombre del Pokémon seleccionado: {pokemon}")
    return pokemon

def select_move(moves):
    moveToUse = int(input(" Seleccione un ataque a ejecutar: "))
    while (moveToUse not in range(len(moves))):
        print("El ataque seleccionado no existe... porfavor seleccione un movimiento existente")
        moveToUse = int(input(" Seleccione un ataque a ejecutar: "))
    return get_move(moves[moveToUse])


#Ingrese el nombre a atacar Pokémon: 
#Ingrese el nombre del primer Pokémon: 