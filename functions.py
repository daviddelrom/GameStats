from classes import Player, Game, Rules, Houses, ResultsClass
from datetime import datetime

def add_player():
    player_name = input("Para añadir un jugador, por favor indica su nombre: ")
    player_abrv = input("Por favor facilita su abreviatura: ")
    playerInstance = Player(player_name, player_abrv)
    return playerInstance

def add_game():
    print("Vamos a crear una partida")
    date = ask_date()
   # rules = ask_rules()
    results = ask_results()
    game = Game(results, date)
    return game


def ask_results():
    print("Vamos a añadir los resultados: ")
    nplayers = int(input("Numero de jugadores:"))
    results = []
    for i in range(nplayers):
        playerabbrv = input(f"Abreviatura del Jugador en posicion {i+1}")
        playerhouse = ask_house()
        results.append(ResultsClass(playerabbrv,i, playerhouse))
    return results

def ask_house():
    while True:
        house_char = input("Dime la casa de tu jugador" ).lower()
        for j in Houses:
            if j.value[0].lower() == house_char:
                return j
        print("casa no encontrada")

def ask_rules():
    options = [i.value for i in Rules]
    print(f"Reglas de la partida disponibles: {', '.join(options)} primera letra")
    while True:
        rules_char = input("Dime la reglas elegidas: ")[0].lower()
        if any(rules_char == j[0].lower() for j in options):
            return Rules.j
        else: print("No especificaste regla correcta")

def ask_date():
    while True:
        date_str = input("Fecha en formato DD/MM/AA por favor: ")
        try:
            fecha = datetime.strptime(date_str, "%d/%m/%y")
            return fecha
        except ValueError:
            print("Formato erroneo, vuelve a probar")