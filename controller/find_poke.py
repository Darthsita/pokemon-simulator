from models import Poke
from cli import input_poke_name

def map_poke_row_to_object(row):
    return Poke(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

def find_one_poke(pokemon_name, libro):
    pokemon = None
    for str_row in libro:
        list_row = str_row.strip().split(",")
        if (list_row[0] == pokemon_name):
            pokemon = map_poke_row_to_object(list_row)
    while (pokemon == None):
        pokemon = error_poke_not_in_libro(libro)
    return pokemon

def error_poke_not_in_libro(libro):
    libro.close()
    libro = open("./data/pokemon_data.csv", "r")
    pokemon_name = input_poke_name("El pokemon seleccionado anteriormente no existe... Por favor intentelo nuevamente: ")
    for str_row in libro:
        list_row = str_row.strip().split(",")
        if (list_row[0] == pokemon_name):
            pokemon = map_poke_row_to_object(list_row)
            return pokemon

def find_many_Poke(pokemons, libro):
    pokemonsUsuario = []
    for str_row in libro:
        list_row = str_row.strip().split(",")
        if (list_row[0] in pokemons):
            pokemonsUsuario.append(map_poke_row_to_object(list_row))
    return pokemonsUsuario