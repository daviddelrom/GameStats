import sqlite3
from sql_queries import SHOW_PLAYERS_LIST, DELETE_PLAYER

class dbmmanager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    def dbstart(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
    def dbclose(self):
        if self.conn is not None:
            self.cursor.close()
            self.conn.close()
            self.cursor = None
            self.conn = None
    def create_tables(self):
        self.dbstart()
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS PLAYERS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    abrv TEXT
                );
                ''')

                # Crear la tabla GAMES
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS GAMES (
                    id INTEGER PRIMARY KEY,
                    fecha TEXT,
                    rules TEXT,
                    nplayers INTEGER
                );
                ''')

                # Crear la tabla RESULTS
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS RESULTS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    game_id INTEGER,
                    pos INTEGER,
                    player_name TEXT,
                    house TEXT,
                    FOREIGN KEY (game_id) REFERENCES GAMES(id)
                    FOREIGN KEY (player_name) REFERENCES PLAYERS(name)
                );
                ''')

            self.conn.commit()
        except sqlite3.Error as e: print("Error1")
        finally: self.dbclose()
    def insert_player(self, player):
        try:
            self.dbstart()
            self.cursor.execute('''
                INSERT INTO PLAYERS (name, abrv)
                VALUES (?, ?)
            ''', (player.name, player.abrv))
            self.conn.commit()
        except sqlite3.Error as e: print("Error2")
        finally: self.dbclose()
    def insert_game(self, game):
        try:
            self.dbstart()
            self.cursor.execute('''
            INSERT INTO GAMES (fecha, rules, nplayers, id)
            VALUES (?,?,?,?)
            ''', (game.date, game.rules, game.nplayers, game.game_id))
            self.conn.commit()
        except sqlite3.Error as e: print("Error3")
        finally: self.dbclose()
    def insert_results(self, game):
        try:
            self.dbstart()
            for result in game.results:
                self.cursor.execute('''
                INSERT INTO RESULTS (game_id, player_name, pos, house)
                VALUES (?,?,?,?)
                ''',(game.game_id, result.player.name, result.pos, result.house.value))
            self.conn.commit()
        except sqlite3.Error as e: print(f"Error al insertar resultados en la base de datos: {e}")
        finally: self.dbclose()

    def list_players(self):
        from classes import Player
        players = []
        try:
            self.dbstart()
            self.cursor.execute(SHOW_PLAYERS_LIST)
            rows = self.cursor.fetchall()
            for row in rows:
                player = Player(*row)
                players.append(player)
        except sqlite3.Error as e: print(f"Error al insertar resultados en la base de datos: {e}")
        finally: 
            self.dbclose()
        return players

    def delete_player(self, abrv):
        try:
            self.dbstart()
            self.cursor.execute(DELETE_PLAYER, (abrv, ))
            self.conn.commit()
        except sqlite3.Error as e: print(f"Error al eliminar jugador: {e}")
        finally: 
            self.dbclose()