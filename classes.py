from enum import Enum

class Player:
    def __init__(self, name, abrv):
        self.name = name
        self.abrv = abrv
    def __str__(self):
        return f"Jugador: {self.name} (Abreviatura: {self.abrv})"
class Game:
    def __init__(self, results, date, rules="Classic" ):
        self.results = results
        self.date = date
        self.rules = rules
    def __str__(self):
        results_str = "\n".join(str(result) for result in self.results)
        return f"Juego - Fecha: {self.date.strftime('%d/%m/%Y')}\n" \
               f"Reglas: {self.rules}\n" \
               f"Resultados:\n{results_str}"

class ResultsClass:
    def __init__(self, player, pos, house):
        self.player = player
        self.pos = pos
        self.house = house
    def __str__(self):
        return f"Posición {self.pos}: {self.player} (Casa: {self.house.value})"

class Rules(Enum):
    Classic = "Clasicas"
    MoD = "Madre de Dragones"
    AFC = "Festin de Cuervos"
    ADWD = "Danza de Dragones"
class Houses(Enum):
    S = "Stark"
    B = "Baratheon"
    L = "Lannister"
    T = "Tyrell"
    G = "Greyjoy"
    M = "Martell"
    A = "Arryn"