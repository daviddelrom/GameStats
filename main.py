from functions import add_player, add_game

def main():
    njugadores = int(input("Cuantos jugadores: "))
    jugadores = []
    for i in range(njugadores):
        jugadores.append(add_player())
    games = []
    npartidas = int(input("Cuantas partidas: "))
    for n in range(npartidas):
        games.append(add_game(jugadores))
    for i in range(njugadores):
        print(jugadores[i])
    for i in range(npartidas):
        print(games[i])
if __name__ == "__main__":
    main()