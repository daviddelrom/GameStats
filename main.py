from functions import add_player, add_game
from classes import Ranking
from bbdd import dbmmanager
def main():
    njugadores = int(input("Cuantos jugadores: "))
    jugadores = []
    db = dbmmanager("agot.db")
    db.create_tables()
    for i in range(njugadores):
        templayer = add_player()
        jugadores.append(templayer)
        db.insert_player(templayer)
    games = []
    npartidas = int(input("Cuantas partidas: "))
    for n in range(npartidas):
        tempgame = add_game(jugadores, n)
        games.append(tempgame)
        db.insert_game(tempgame)
        db.insert_results(tempgame)
    for i in range(njugadores):
        print(jugadores[i])
    for i in range(npartidas):
        print(games[i])
    rank = Ranking(games, jugadores)
    print(rank)
if __name__ == "__main__":
    main()