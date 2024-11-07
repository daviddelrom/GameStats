from classes import Player, Game, Rules, Houses, ResultsClass
from datetime import datetime

def add_player():
    player_name = input("Para añadir un jugador, por favor indica su nombre: ")
    player_abrv = input("Por favor facilita su abreviatura: ")
    newplayer = Player(player_name, player_abrv)
    return newplayer

def add_game(players):
    print("Vamos a crear una partida")
    date = ask_date()
    results = ask_results(players)
    want_rules = input("Deseas especificar reglas? (s/n)").lower()
    if want_rules == 's':
        rules = ask_rules()
        game = Game(results, date, rules)
    else: game = Game(results, date)
    return game


def ask_results(players):
    print("Vamos a añadir los resultados: ")
    nplayers = int(input("Numero de jugadores:"))
    results = []
    playername = ""
    for i in range(nplayers):
        playerabbrv = input(f"Abreviatura del Jugador en posicion {i+1}")
        playerhouse = ask_house()
        for player in players:
            if playerabbrv == player.abrv:
                results.append(ResultsClass(player,i, playerhouse))
    
    return results

def ask_house():
    while True:
        house_char = input("Dime la casa de tu jugador" )[0].lower()
        for j in Houses:
            if j.value[0].lower() == house_char:
                return j
        print("casa no encontrada")

def ask_rules():
    while True:
        rules_char = input("Que reglas deseas usar")[0].lower()
        for j in Rules:
            if j.value[0].lower() == rules_char:
                return j
   
def ask_date():
    while True:
        date_str = input("Fecha en formato DD/MM/AA por favor: ")
        try:
            fecha = datetime.strptime(date_str, "%d/%m/%y")
            return fecha
        except ValueError:
            print("Formato erroneo, vuelve a probar")