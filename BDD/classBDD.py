
import sqlite3
from datetime import date
#On set up une BDD avec plusieurs tables

class BDD_Manager:
    def __init__(self,path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.create_stations_table()
        
    def create_stations_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Station (
            id TEXT PRIMARY KEY,
            nom_station TEXT,
            capacite INTEGER,
            coordonnees_station TEXT,
            id_commune TEXT,
            en_fonctionnement BOOLEAN,
            date_deb DATE,
            date_fin DATE,
            borne_paiement BOOLEAN,
            nb_bornettes INT
            
        )
        """)
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Temps (
            id_temps TIMESTAMP PRIMARY KEY,
            date TEXT,
            annee INT,
            mois INT,
            jour INT,
            heure INT,
            minute INT            
        )
        """)
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS StationFaits (
            id_station TEXT PRIMARY KEY,
            nb_bornettes INT,
            velos_dispos INT,
            meca_dispo INT,
            elec_dispo INT,
            retour_velo BOOL,
            frequence INT,
            date_fait_deb TIMESTAMP,
            date_fait_fin TIMESTAMP            
        )
        """)
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Commune (
            id_commune TEXT PRIMARY KEY,
            nom_commune TEXT            
        )
        """)
        self.conn.commit()
    
    def close(self):
        self.conn.close()

# db_manager = BDD_Manager(BDD_PATH)
# db_manager.create_stations_table()
# db_manager.close()

#question : on a trois table, est ce qu'il ne faut pas passer en argument le nom de la table dans create table pour pouvoir en créer
#d'autres ? ou faut il creer deux autre fonnctions create table ?