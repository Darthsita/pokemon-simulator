class Poke:
    def __init__(self, name, tipo, hp, atk, defen, atkesp, defesp, vel, moves):
        self.name = name
        self.tipo = tipo
        self.hpBase = hp
        self.atkBase = atk
        self.defBase = defen
        self.atkespBase = atkesp
        self.defespBase = defesp
        self.velBase = vel
        self.hpIVTotal = calculateHP(hp)
        self.hpIVActual = calculateHP(hp)
        self.atkIV = calculateStats(atk)
        self.defIV = calculateStats(defen)
        self.atkespIV = calculateStats(atkesp)
        self.defespIV = calculateStats(defesp)
        self.velIV = calculateStats(vel)
        self.moves = str(moves).split(";")

    def __str__(self):
        return f"""
        ________________________________________________________________________________________
        Name: {self.name},
        El HP al nivel 50 de {self.name} es : {self.hpIVTotal}/{self.hpIVActual}
        El ATK al nivel 50 de {self.name} es : {self.atkIV}
        El DEF al nivel 50 de {self.name} es : {self.defIV}
        El ATK ESP al nivel 50 de {self.name} es : {self.atkespIV}
        El DEF ESP al nivel 50 de {self.name} es : {self.defespIV}
        El SPE al nivel 50 de {self.name} es : {self.velIV}
        ________________________________________________________________________________________
        """

    def dicctonary(self):
        statsBase = {
        "NAME": self.name,
        "HP_base": self.hpBase,
        "ATK": self.atkBase,
        "DEF": self.defBase,
        "ATKESP": self.atkespBase,
        "DEFESP": self.defespBase,
        "VEL": self.velBase
                }
        return statsBase
        
    def print_pokemon_defensor(self):
        print(f"El hp a nivel 50 de {self.name} es {self.hpIVTotal}/{self.hpIVActual} ")


def calculateHP(hp):
    aux = (round(((((int(hp) + 31)*2 + ((250**0.5)/4))* 50)/100) + 50 + 10, 2))
    return aux
def calculateStats(stat):
    aux = (round(((((int(stat) + 31)*2 + ((250**0.5)/4))* 50)/100) + 5, 2))
    return aux
