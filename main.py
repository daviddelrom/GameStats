from functions import add_player, add_game

def main():
    print("POC del gestor de partidas DDR")
    jugadores = []
    jugadores.append(add_player())
    games = []
    games.append(add_game())
    print(jugadores[0])
    print(games[0])
if __name__ == "__main__":
    main()