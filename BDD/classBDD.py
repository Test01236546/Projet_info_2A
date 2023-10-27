
import sqlite3
from datetime import date
#test

class Jer_BDD:
    def __init__(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            id TEXT PRIMARY KEY,
            nom_station TEXT,
            capacite INTEGER,
            coordonnees_station TEXT,
            nom_commune TEXT,
            en_fonctionnement BOOLEAN,
            date_deb DATE,
            date_fin DATE,
            borne_paiement BOOLEAN,
            nb_bornettes INTEGER
        )
        """)
        self.conn.commit()
