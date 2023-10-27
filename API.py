from fastapi import FastAPI

import requests as r 
from pydantic import BaseModel
from Service.Station import Station
import uvicorn
from Service.Service import Service
from datetime import datetime
import Service.Fonctionnalites as F
from geopy.geocoders import Nominatim 

app=FastAPI()
# Classe API
class StationAPI():
    def __init__(self):
        super().__init__()
        #self.station = Station()
        self.connection = None

    def station_plus_proche(self, adresse):
        # Récupération des données de l'API
        url = "https://api-adresse.data.gouv.fr/search/?q={}".format(adresse)
        response = r.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data["features"]) == 1:
                position = (data["features"][0]["geometry"]["coordinates"][0], data["features"][0]["geometry"]["coordinates"][1])
                # Appeler la méthode F1() de la classe Fonctionnalites()
                station_proche = F.Fonctionnalites().F1(lat, lon)

                return station_proche
            else:
                raise Exception("L'adresse donnée n'est pas valide")
        else:
            raise Exception("Erreur lors de la récupération des données de l'API Adresse")


    def get_station_la_moins_frequentee(self, date_debut, date_fin):
        # Récupération des données de la base de données
        return dao.least_frequented_station
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM stations WHERE date_update BETWEEN ? AND ? ORDER BY available_bikes DESC", (date_debut, date_fin))
        data = cursor.fetchone()
        cursor.close()

        # Retour de la station la moins fréquentée
        return data[0] if data is not None else None

    def get_arrondissement_le_plus_frequente(self, date_debut, date_fin):
        # Récupération des données de la base de données
        return dao.most_frequented_arr()

        cursor = self.connection.cursor()
        cursor.execute("SELECT arrondissement, COUNT(*) AS nb_usagers FROM stations WHERE date_update BETWEEN ? AND ? GROUP BY arrondissement ORDER BY nb_usagers DESC", (date_debut, date_fin))
        data = cursor.fetchone()
        cursor.close()

        # Retour de l'arrondissement le plus fréquenté
        return data[0] if data is not None else None
    
    
@app.get("/")
def get_stations():
    return "Working"

@app.get("/stations")
def get_stations():
    return Station().get_stations()

@app.get("/stations/closest")
def get_closest_station(adresse):
    return F.Fonctionnalites().F1(adresse)

@app.get("/stations/least_frequented")
def get_least_frequented_station(start_date: str, end_date: str):
    return Station().get_least_frequented_station(start_date, end_date)

@app.get("/stations/most_frequented_arrondissement")
def get_most_frequented_arrondissement(start_date: str, end_date: str):
    return Station().get_most_frequented_arrondissement(start_date, end_date)






def get_position_from_address(address):
    # Récupération des données de l'API
    url = "https://api-adresse.data.gouv.fr/search/?q={}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data["features"]) == 1:
            position = (data["features"][0]["geometry"]["coordinates"][0], data["features"][0]["geometry"]["coordinates"][1])
            return position
        else:
            raise Exception("L'adresse donnée n'est pas valide")
    else:
        raise Exception("Erreur lors de la récupération des données de l'API Adresse")

if __name__ == "__main__":
    position = get_position_from_address(address)
    print(position)
