import sqlite3
from tools import mytools as mt, const


def ausgabe(cursor):
    # SQL-Abfrage, senden, Ausgabe
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
    print()


def main():
    mt.h1("sqlite loeschen")

    # Verbindung, Cursor
    connection = sqlite3.connect(const.temp+"/firma.db")
    cursor = connection.cursor()

    # Datensatz erzeugen
    sql = "INSERT INTO personen VALUES('Maier2', " \
        "'Hans', 8888, 3500, '15.03.1962')"
    cursor.execute(sql)
    connection.commit()
    # Vorher
    ausgabe(cursor)

    # Datensatz entfernen
    sql = "DELETE FROM personen " \
        "WHERE personalnummer = 8888"
    cursor.execute(sql)

    connection.commit()

    # Nachher
    ausgabe(cursor)

    connection.close()

    mt.end(__name__)

if __name__ == "__main__":
    main()
