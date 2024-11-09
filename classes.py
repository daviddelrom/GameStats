from enum import Enum
from datetime import datetime
from bbdd import dbmmanager
class Player:
    def __init__(self, name, abrv):
        self.name = name
        self.abrv = abrv
    def __str__(self):
        return f"Jugador: {self.name} (Abreviatura: {self.abrv})"
    @staticmethod
    def add_player():
        player_name = input("Para añadir un jugador, por favor indica su nombre: ")
        player_abrv = input("Por favor facilita su abreviatura: ")
        newplayer = Player(player_name, player_abrv)
        return newplayer

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
    
    def add_game(self, players, game_id):
        print("Vamos a crear una partida")
        date = datetime.now()
        results = ask_results(players)
        want_rules = input("Deseas especificar reglas? (s/n)").lower()
        if want_rules == 's':
            rules = self.ask_rules()
            game = Game(results, game_id, date, rules)
        else: game = Game(results, game_id, date)
        return game

    @staticmethod
    def ask_rules():
        while True:
            rules_char = input("Que reglas deseas usar")[0].lower()
            for j in Rules:
                if j.value[0].lower() == rules_char:
                    return j

    @staticmethod
    def ask_date():
        while True:
            date_str = input("Fecha en formato DD/MM/AA por favor: ")
            try:
                fecha = datetime.strptime(date_str, "%d/%m/%y")
                return fecha
            except ValueError:
                print("Formato erroneo, vuelve a probar")

class ResultsClass:
    def __init__(self, player, pos, house):
        self.player = player
        self.pos = pos
        self.house = house
    def __str__(self):
        return f"Posición {self.pos+1}: {self.player.name} (Casa: {self.house.value})"

    def ask_results(self, players):
        print("Vamos a añadir los resultados: ")
        nplayers = int(input("Numero de jugadores:"))
        results = []
        playername = ""
        for i in range(nplayers):
            playerabbrv = input(f"Abreviatura del Jugador en posicion {i+1}")
            playerhouse = self.ask_house()
            for player in players:
                if playerabbrv == player.abrv:
                    results.append(ResultsClass(player,i, playerhouse))
        
        return results
    @staticmethod
    def ask_house():
        while True:
            house_char = input("Dime la casa de tu jugador" )[0].lower()
            for j in Houses:
                if j.value[0].lower() == house_char:
                    return j
            print("casa no encontrada")
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

class Menu:
    @staticmethod
    def showmenu():
        print('''Bienvenido a GameManager:\n
        a) Añadir jugadores\n
        b) Borrar jugadores\n
        c) Crear una nueva partida\n
        d) Ver jugadores\n
        e) Ver partidas\n''')
    @staticmethod
    def getoption(db):
        option = input("Selecciona una opcion por favor: ").lower()
        if option == 'a':
            player = Player.add_player()
            db.insert_player(player)
    #   else if option == 'b':
    #  else if option == 'c':
    #  else if option == 'd':
    # else if option == 'e':
