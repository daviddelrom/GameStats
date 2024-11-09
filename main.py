from classes import Menu
from bbdd import dbmmanager
def main():
    db = dbmmanager("agot.db")
    db.create_tables()
    Menu.showmenu()
    Menu.getoption(db)
if __name__ == "__main__":
    main()