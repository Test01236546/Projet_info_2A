
import sqlite3
from datetime import date
#test
DB_PATH = "Test_Jeremie/test.sql"

class BDD_Manager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
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
    
    def close(self):
        self.conn.close()

db_manager = BDD_Manager("ma_base_de_donnees.sqlite")
db_manager.create_stations_table()
db_manager.close()
