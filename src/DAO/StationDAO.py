import sqlite3
from datetime import datetime
#import sys
import src.Service.Station as st
import json
import src.Service.fonctions_intermediaires as fi
from src.DAO.AbstractDAO import AbstractDAO

class StationDAO(AbstractDAO):
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
        self.path = "BDD/BDD.sql"

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

    def create2(self,dictionnaire):         
        
        Station_to_add=st.Station(dictionnaire['stationcode'],dictionnaire['name'],dictionnaire['capacity'],json.dumps(dictionnaire['coordonnees_geo']),fi.afficher_nom_commune_complete(dictionnaire['stationcode']),dictionnaire['is_renting'],dictionnaire['duedate'],f"date_deb {dictionnaire['stationcode']}",f"borne_paiement {dictionnaire['stationcode']}",dictionnaire['capacity'])
        # return Station_to_add
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
    
    def update2(self, dictionnaire):
        """
        Met à jour les informations d'une station dans la base de données en utilisant les données fournies dans un dictionnaire.

        Args:
            dictionnaire (dict): Un dictionnaire contenant les nouvelles données de la station.
        """
        # Création d'une instance de Station avec les données mises à jour
        Station_to_update = st.Station(
            dictionnaire['stationcode'],
            dictionnaire['name'],
            dictionnaire['capacity'],
            json.dumps(dictionnaire['coordonnees_geo']),
            fi.afficher_nom_commune_complete(dictionnaire['stationcode']),
            dictionnaire['is_renting'],
            dictionnaire['duedate'],
            f"date_deb {dictionnaire['stationcode']}",
            f"borne_paiement {dictionnaire['stationcode']}",
            dictionnaire['capacity']
        )

        # Mise à jour de l'enregistrement dans la base de données
        self.cur.execute("""
        UPDATE Station SET nom_station=?, capacite=?, coordonnees_station=?, 
        id_commune=?, en_fonctionnement=?, date_deb=?, date_fin=?, 
        borne_paiement=?, nb_bornettes=? WHERE id=?
        """, (
            Station_to_update.nom_station,
            Station_to_update.capacite,
            Station_to_update.coordonnees_station,
            Station_to_update.id_commune,
            Station_to_update.en_fonctionnement,
            Station_to_update.date_deb,
            Station_to_update.date_fin,
            Station_to_update.borne_paiement,
            Station_to_update.nb_bornettes,
            Station_to_update.id
        ))
        self.conn.commit()
        print(f"Station {Station_to_update.id} mise à jour")

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


    def upsert2(self, dictionnaire):

        # Construction de la requête pour vérifier l'existence de l'élément
        self.cur.execute("SELECT * FROM Station WHERE id=?", (dictionnaire['stationcode'],))
        existing_record = self.cur.fetchone()
        
        # Création d'une instance de Station
        Station_to_upsert = st.Station(
            id=dictionnaire['stationcode'],
            nom_station=dictionnaire['name'],
            capacite=dictionnaire['capacity'],
            coordonnees_station=json.dumps(dictionnaire['coordonnees_geo']),
            id_commune=fi.codeInsee_to_code(dictionnaire['stationcode']),
            en_fonctionnement=dictionnaire['is_renting'],
            date_deb=datetime.now(),
            date_fin=dictionnaire['duedate'],
            borne_paiement=f"borne_paiement {dictionnaire['stationcode']}",
            nb_bornettes=dictionnaire['capacity']
        )

        if existing_record :
            # Si l'enregistrement existe, créer une instance de StationFaits avec les données existantes
            # print(existing_record)
            former_Station = st.Station(id=existing_record[0],nom_station=existing_record[1],capacite=existing_record[2],coordonnees_station=existing_record[3],id_commune=existing_record[4],en_fonctionnement=existing_record[5],date_deb=existing_record[6],date_fin=existing_record[7],borne_paiement=existing_record[8],nb_bornettes=existing_record[9])
            # Tentative de mise à jour
            self.cur.execute("""
            UPDATE Station SET nom_station=?, capacite=?, coordonnees_station=?, id_commune=?,
            en_fonctionnement=?, date_deb=?, date_fin=?, borne_paiement=?, nb_bornettes=? WHERE id=?
            """, (
                Station_to_upsert.nom_station,
                Station_to_upsert.capacite,
                Station_to_upsert.coordonnees_station,
                Station_to_upsert.id_commune,
                Station_to_upsert.en_fonctionnement,
                former_Station.date_fin,            # date debut du new = date fin ancien
                Station_to_upsert.date_fin,
                Station_to_upsert.borne_paiement,
                Station_to_upsert.nb_bornettes,
                Station_to_upsert.id
            ))

        else :
            self.cur.execute("""
            INSERT INTO Station VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                Station_to_upsert.id,
                Station_to_upsert.nom_station,
                Station_to_upsert.capacite,
                Station_to_upsert.coordonnees_station,
                Station_to_upsert.id_commune,
                Station_to_upsert.en_fonctionnement,
                Station_to_upsert.date_deb,
                Station_to_upsert.date_fin,
                Station_to_upsert.borne_paiement,
                Station_to_upsert.nb_bornettes
            ))

        self.conn.commit()
        # print(f"Station {Station_to_upsert.id} mise à jour ou insérée")

    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

