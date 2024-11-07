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
        self.nplayers = len(results)
    def __str__(self):
        results_str = ""
        for result in self.results:
            results_str += str(result) + f" Pts: {pts.static(result.pos, self.nplayers)}" + "\n"
        return f"Juego - Fecha: {self.date.strftime('%d/%m/%Y')}\n" \
           f"Reglas: {self.rules}\n" \
           f"Resultados:\n{results_str}"


class ResultsClass:
    def __init__(self, player, pos, house):
        self.player = player
        self.pos = pos
        self.house = house
    def __str__(self):
        return f"Posición {self.pos+1}: {self.player.name} (Casa: {self.house.value})"

class pts:
    def static(pos, nplayers):
        if pos+1 == 1:
            return nplayers + 2
        elif pos+1 == 2:
            return nplayers
        else:
            return nplayers - pos
    def dynamic(pos, nplayers, self_part, total_part):
        st_pts = static(pos, nplayers)
        coef = 10 - (total_part - self_part)
        if coef > 0:
            return st_pts * coef
        else: return st_pts

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