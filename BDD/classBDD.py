
import sqlite3
from datetime import date
#test
BDD_PATH = "Test_Jeremie/test1.sql"

class BDD_Manager:
    def __init__(self,path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.create_stations_table()
        
    def create_stations_table(self):
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

db_manager = BDD_Manager(BDD_PATH)
db_manager.create_stations_table()
db_manager.close()

#question : on a trois table, est ce qu'il ne faut pas passer en argument le nom de la table dans create table pour pouvoir en créer
#d'autres ? ou faut il creer deux autre fonnctions create table ?