import requests
import pyodbc
from datetime import datetime
import os
import sys
from BDD.constantes import BDD_PATH
# sys.path.append('../DAO/StationDAO')

from DAO import StationDAO as stDAO
from DAO import communeDAO as cmDAO
from DAO import TempsDAO as tpDAO
from DAO import StationFaitsDAO as stfDAO 




class Jer_Service ():
    def __init__(self):
        #self.id_stationfaits=id_stationfaits
        #self.id_station=id_station
        #self.id_temps=id_temps
        #self.connection = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=velib;UID=sa;PWD=password")
        pass
    
    def ingest():
    # Obtenir les données de l'API Vélib
        url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Erreur lors de la requête à l'API Vélib.")
            return

    # Ouvrir les bases de données
        Instance_StationDAO = stDAO.StationDAO(BDD_PATH)
        Instance_CommuneDAO = cmDAO.CommuneDAO(BDD_PATH)
        Instance_TempsDAO = tpDAO.TempsDAO(BDD_PATH)
        Instance_StationFaitsDAO = stfDAO.StationFaitsDAO(BDD_PATH)

    #data a deux clés (total et results), results est une liste de dictionnaires dons les keys-values sont des infos sur la station
    #ON VA VECTORISER LES CLACULS AVEC UN APPLY, on fait un create2 qui créé directement la station(resp le reste) puis la met dans la table


    # Mettre à jour les bases de données
        for station in data['results']:
        # Vérifier si la station existe déjà dans la base de données stations
            cur_station.execute("SELECT * FROM stations WHERE id=?", (station['id'],))
            station_exists = cur_station.fetchone()

        # Si la station n'existe pas, la créer
            if not station_exists:
                self.create_station(station)
            else:
            # Si la station existe, la mettre à jour
                self.update_station(station)

        # Mettre à jour l'état de la station
            self.update_etat_station(station)

        

#TESTS
data['total_count']
type(data['results'])       #c'est une liste
data['results'][0]  
"""
>>> {'stationcode': '16107', 'name': 'Benjamin Godard - Victor Hugo', 'is_installed': 'OUI', 'capacity': 35, 'numdocksavailable': 26,
 'numbikesavailable': 9, 'mechanical': 3, 'ebike': 6, 'is_renting': 'OUI', 'is_returning': 'OUI', 'duedate': '2023-11-08T14:43:03+01:00',
   'coordonnees_geo': {'lon': 2.275725, 'lat': 48.865983}, 'nom_arrondissement_communes': 'Paris', 'code_insee_commune': None}
"""       


#if __name__ == "__main__":
#    service = Service()
#    service.ingest()


