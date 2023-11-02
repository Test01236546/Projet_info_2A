import sqlite3
from datetime import date
import sys


class StationDAO:
    def __init__(self,path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self, station):
        self.cur.execute("""
        INSERT INTO Station VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (station.id, station.nom_station, station.capacite, station.coordonnees_station, 
              station.nom_commune, station.en_fonctionnement, station.date_deb, station.date_fin, 
              station.borne_paiement, station.nb_bornettes,))
        self.conn.commit()
        print(f"Station créée : {station.id}")

    def read(self, id):
        self.cur.execute("SELECT * FROM Station WHERE id=?", (id,))
        station = self.cur.fetchone()
        if station:
            print("Station trouvée:", station)
            return station
        else:
            print("Station non trouvée")
            return None

    def update(self, id, new_data):
        self.cur.execute("""
        UPDATE Station SET nom_station=?, capacite=?, coordonnees_station=?, 
        nom_commune=?, en_fonctionnement=?, date_deb=?, date_fin=?, 
        borne_paiement=?, nb_bornettes=? WHERE id=?
        """, (new_data.nom_station, new_data.capacite, new_data.coordonnees_station, 
              new_data.nom_commune, new_data.en_fonctionnement, new_data.date_deb, 
              new_data.date_fin, new_data.borne_paiement, new_data.nb_bornettes, id))
        self.conn.commit()
        print(f"Station {id} mise à jour")
    


    def delete(self, id):
        self.cur.execute("DELETE FROM Station WHERE id=?", (id,))
        self.conn.commit()
        print(f"Station {id} supprimée")


# def update2(self, id, new_data):
#     self.cur.execute("""
#     UPDATE Station SET nom_station=?, capacite=?, coordonnees_station=?, 
#     nom_commune=?, en_fonctionnement=?, date_deb=?, date_fin=?, 
#     borne_paiement=?, nb_bornettes=? WHERE id=?
#     """, (new_data['nom_station'], new_data['capacite'], new_data['coordonnees_station'], 
#             new_data['nom_commune'], new_data['en_fonctionnement'], new_data['date_deb'], 
#             new_data['date_fin'], new_data['borne_paiement'], new_data['nb_bornettes'], id))
#     self.conn.commit()
#     print("Station mise à jour")