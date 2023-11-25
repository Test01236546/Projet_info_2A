import requests
import json
from src.BDD.constantes import BDD_PATH

# from Service import Station as st
# from Service import commune as cm
# from Service import Temps as tp
# from Service import StationFaits as stf

from src.DAO import StationDAO as stDAO
from src.DAO import communeDAO as cmDAO
from src.DAO import TempsDAO as tpDAO
from src.DAO import StationFaitsDAO as stfDAO

from src.Service.fonctions_intermédiaires import no_print_map,no_print_map2

# from BDD import classBDD as cBDD

class Service ():
    """
    Crée la classe Service qui permet de mettre à jour la base de données
    """
    def __init__(self):
        """
        Initialise un objet Service pour l'ingestion de données depuis l'API Vélib'.

        Note:
            Cette classe est destinée à être utilisée pour l'ingestion de données depuis l'API Vélib'.
        """
        self.url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"
        self.Instance_StationDAO = stDAO.StationDAO(BDD_PATH)
        self.Instance_CommuneDAO = cmDAO.CommuneDAO(BDD_PATH)
        self.Instance_TempsDAO = tpDAO.TempsDAO(BDD_PATH)
        self.Instance_StationFaitsDAO = stfDAO.StationFaitsDAO(BDD_PATH)
        
        #self.id_stationfaits=id_stationfaits
        #self.id_station=id_station
        #self.id_temps=id_temps
        #self.connection = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=velib;UID=sa;PWD=password")
        pass
    
    def ingest(self):
        """
        Ingestion des données depuis l'API Vélib' et mise à jour des bases de données locales.

        Cette méthode effectue les opérations suivantes :
        1. Récupère les données depuis l'API Vélib'.
        2. Ouvre les bases de données locales pour les stations, les faits de station, les communes et le temps.
        3. Met à jour les bases de données locales en ajoutant ou mettant à jour les stations.
        4. Met à jour l'état des stations.
        5. Commit les modifications dans les bases de données locales.
        6. Ferme les connexions aux bases de données locales.

        Note:
            Les fichiers "Station.sql", "StationFaits.sql", "Commune.sql", et "Temps.sql" doivent être présents 
            et contenir les scripts SQL pour créer les tables correspondantes dans les bases de données locales.
        """
        
        response = requests.get(self.url)       # mettre ça au début avant le init ?
        if response.status_code == 200:
            data = response.json()
        else:
            raise Exception("Erreur lors de la requête à l'API Vélib.")

        # Instance_StationDAO = stDAO.StationDAO(BDD_PATH)
        # Instance_CommuneDAO = cmDAO.CommuneDAO(BDD_PATH)
        # Instance_TempsDAO = tpDAO.TempsDAO(BDD_PATH)
        # Instance_StationFaitsDAO = stfDAO.StationFaitsDAO(BDD_PATH)

        no_print_map2(map(lambda station_dict: self.Instance_StationDAO.upsert2(station_dict), data['results']))
        no_print_map2(map(lambda station_dict: self.Instance_CommuneDAO.upsert2(station_dict), data['results']))
        no_print_map2(map(lambda station_dict: self.Instance_TempsDAO.upsert2(station_dict), data['results']))
        no_print_map2(map(lambda station_dict: self.Instance_StationFaitsDAO.upsert2(station_dict), data['results']))


        
        



#if __name__ == "__main__":
#    service = Service()
#    service.ingest()


