import sqlite3
from datetime import date
import sys
import Service.Station as st


class StationDAO:
    """
    Crée la classe StationDAO qui permet de mettre à jour la table Station dans la base de données
    """
    def __init__(self,path):
        """
        Initialise un objet d'accès aux données (DAO) pour la table 'Station' dans une base de données SQLite.

        Args:
            path (str): Le chemin du fichier de base de données SQLite.
        """
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self, station):
        """
        Crée un enregistrement de station dans la base de données.

        Args:
            station (Station): L'objet Station à insérer dans la base de données.
        """
        self.cur.execute("""
        INSERT INTO Station VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (station.id, station.nom_station, station.capacite, station.coordonnees_station, 
              station.id_commune, station.en_fonctionnement, station.date_deb, station.date_fin, 
              station.borne_paiement, station.nb_bornettes,))
        self.conn.commit()
        print(f"Station créée : {station.id}")

    def create2(self,dict):         #on pourrait prendre deux liste (nom attributs de StationFaits, nom clées du dict station et matcher)
        Station_to_add=st.Station(dict['stationcode'],dict['name'],dict['capacity'],dict['coordonnees_geo'],dict['code_insee_commune'],dict['is_renting'],dict['duedate'],f"date_deb {dict['stationcode']}",f"borne_paiement {dict['stationcode']}",dict['capacity'])
        self.cur.execute("""
        INSERT INTO Station VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (Station_to_add.id, Station_to_add.nom_station, Station_to_add.capacite, Station_to_add.coordonnees_station, 
              Station_to_add.id_commune, Station_to_add.en_fonctionnement, Station_to_add.date_deb, Station_to_add.date_fin, 
              Station_to_add.borne_paiement, Station_to_add.nb_bornettes,))
        self.conn.commit()


    def read(self, id):
        """
        Recherche une station dans la base de données en fonction de son identifiant.

        Args:
            id (str): L'identifiant de la station à rechercher.

        Returns:
            tuple or None: Un tuple contenant les données de la station trouvée (id, nom_station, capacite, coordonnees_station, id_commune, en_fonctionnement, date_deb, date_fin, borne_paiement, nb_bornettes) ou None si la station n'a pas été trouvée.
        """
        self.cur.execute("SELECT * FROM Station WHERE id=?", (id,))
        station = self.cur.fetchone()
        if station:
            print("Station trouvée:", station)
            return station
        else:
            print("Station non trouvée")
            return None

    def update(self, id, new_data):
        """
        Met à jour les informations d'une station dans la base de données.

        Args:
            id (str): L'identifiant de la station à mettre à jour.
            new_data (Station): L'objet Station contenant les nouvelles données.

        Note:
            Cette méthode met à jour toutes les colonnes de la table Station en fonction des données fournies.
        """
        self.cur.execute("""
        UPDATE Station SET nom_station=?, capacite=?, coordonnees_station=?, 
        id_commune=?, en_fonctionnement=?, date_deb=?, date_fin=?, 
        borne_paiement=?, nb_bornettes=? WHERE id=?
        """, (new_data.nom_station, new_data.capacite, new_data.coordonnees_station, 
              new_data.id_commune, new_data.en_fonctionnement, new_data.date_deb, 
              new_data.date_fin, new_data.borne_paiement, new_data.nb_bornettes, id))
        self.conn.commit()
        print(f"Station {id} mise à jour")
    


    def delete(self, id):
        """
        Supprime une station de la base de données en fonction de son identifiant.

        Args:
            id (str): L'identifiant de la station à supprimer.
        """
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