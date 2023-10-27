import sqlite3
from datetime import date
from Test_Jeremie.jer_station import jer_station
from Station import Station

DB_PATH = "Test_Jeremie/test.sql"

class jer_stationDAO:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)        #on peut aussi mettre un argument path dans le __init__
        self.cur = self.conn.cursor()
        self.create_table()

    
    def create(self, station: Station):
        self.cur.execute("""
        INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (station.id, station.nom_station, station.capacite, station.coordonnees_station, 
            station.nom_commune, station.en_fonctionnement, station.date_deb, station.date_fin, 
            station.borne_paiement, station.nb_bornettes))
        self.conn.commit()
        print(f"Station {self.nom_station} créée")

    def read(self, id):
        self.cur.execute("SELECT * FROM stations WHERE id=?", (id,))
        station = self.cur.fetchone()
        if station:
            print("Station trouvée:", station)
        else:
            print("Station non trouvée")
        return station

    def update(self, id, new_data: Station):
        # if not isinstance(new_data, jer_station):
        #     print("L'objet fourni n'est pas une instance de la classe Station")
        #     return
    
        self.cur.execute("""
        UPDATE stations SET nom_station=?, capacite=?, coordonnees_station=?, 
        nom_commune=?, en_fonctionnement=?, date_deb=?, date_fin=?, 
        borne_paiement=?, nb_bornettes=? WHERE id=?
        """, (new_data['nom_station'], new_data['capacite'], new_data['coordonnees_station'], 
            new_data['nom_commune'], new_data['en_fonctionnement'], new_data['date_deb'], 
            new_data['date_fin'], new_data['borne_paiement'], new_data['nb_bornettes'], id))
        self.conn.commit()
        print("Station mise à jour")

    def delete(self, id):
        self.cur.execute("DELETE FROM stations WHERE id=?", (id,))
        self.conn.commit()
        print("Station supprimée")

    def injest(self, station):
        self.create(station)


