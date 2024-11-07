from enum import Enum
class Player:
    def __init__(self, name, abrv):
        self.name = name
        self.abrv = abrv
    def __str__(self):
        return f"Jugador: {self.name} (Abreviatura: {self.abrv})"
class Game:
    def __init__(self, results, game_id, date, rules="Classic" ):
        self.results = results
        self.date = date
        self.rules = rules
        self.nplayers = len(results)
        self.game_id = game_id
    def __str__(self):
        results_str = ""
        for result in self.results:
            results_str += str(result) + f" Pts: {Pts.static(result.pos, self.nplayers)}" + "\n"
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

class Pts:
    @staticmethod
    def static(pos, nplayers):
        if pos+1 == 1:
            return nplayers + 2
        elif pos+1 == 2:
            return nplayers
        else:
            return nplayers - pos
    @staticmethod
    def dynamic(pos, nplayers, self_part, total_part):
        st_pts = Pts.static(pos, nplayers)
        coef = 10 - (total_part - self_part)
        if coef > 0:
            return st_pts * coef
        else: return st_pts

class Ranking:

    def __init__(self, games, players):
        self.games = games
        self.players = players
        self.player_pts_dict = self.gen_ranking()
    def gen_ranking(self):
        player_pts_dict = {}
        for player in self.players:
            player_pts = 0
            for game in self.games:
                for plingame in game.results:
                    if plingame.player == player:
                        player_pts+= Pts.dynamic(plingame.pos, len(game.results), game.game_id+1 , len(self.games))
            player_pts_dict[player.name] = player_pts
        return player_pts_dict
    def __str__(self):
        result_str = ""
        for player in self.players:
            result_str += f"Jugador: {player.name} Pts: {self.player_pts_dict[player.name]}\n"
        return result_str
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