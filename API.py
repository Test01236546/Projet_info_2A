from fastapi import FastAPI

import requests
from pydantic import BaseModel
from Station import Station
import uvicorn
from Service import Service

app=FastAPI()
# Classe API
class StationAPI():
    def __init__(self):
        super().__init__()
        self.station = Station()
        self.connection = None

    def get_station_la_plus_proche(self, adresse: str):
        return dao_station_la_plus_proche

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
def get_closest_station(latitude: float, longitude: float):
    return Station().get_closest_station(latitude, longitude)

@app.get("/stations/least_frequented")
def get_least_frequented_station(start_date: str, end_date: str):
    return Station().get_least_frequented_station(start_date, end_date)

@app.get("/stations/most_frequented_arrondissement")
def get_most_frequented_arrondissement(start_date: str, end_date: str):
    return Station().get_most_frequented_arrondissement(start_date, end_date)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

from service import Service


if __name__ == "__main__":
    service = Service()
    service.ingest()
