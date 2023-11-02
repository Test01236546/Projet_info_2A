import requests
import pyodbc
from datetime import datetime
import os
import sys
sys.path.append('../DAO/StationDAO')
import DAO.stationDAO as dao 




class Service ():
    def __init__(self,):
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
        with open("Station.sql", "r") as f:
            sql_station = f.read()
        with open("StationFaits.sql", "r") as f:
            sql_stationFaits = f.read()
        with open("Commune.sql", "r") as f:
            sql_commune = f.read()
        with open("Temps.sql", "r") as f:
            sql_temps = f.read()
        conn_station = sqlite3.connect("stations.db")
        conn_stationFaits = sqlite3.connect("stationFaits.db")
        conn_commune = sqlite3.connect("commune.db")
        conn_temps = sqlite3.connect("temps.db")
        conn_station.executescript(sql_station)
        conn_stationFaits.executescript(sql_stationFaits)
        conn_commune.executescript(sql_commune)
        conn_temps.executescript(sql_temps)
        cur_station = conn_station.cursor()
        cur_stationFaits = conn_stationFaits.cursor()
        cur_commune = conn_commune.cursor()
        cur_temps = conn_temps.cursor()

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

        conn_station.commit()
        conn_stationFaits.commit()
        conn_commune.commit()
        conn_temps.commit()
        conn_station.close()
        conn_stationFaits.close()
        conn_commune.close()
        conn_temps.close()


#if __name__ == "__main__":
#    service = Service()
#    service.ingest()


