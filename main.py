from fastapi import FastAPI

import requests
from pydantic import BaseModel
from Station import Station


app=FastAPI()
# Classe API
class StationAPI(FastAPI):
    def __init__(self):
        super().__init__()
        self.station = Station()
        self.connection = None


    def create_database(self):
        # Connexion à la base de données
        self.connection = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=velib;UID=sa;PWD=password")

        # Création de la table "stations"
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE stations (id INT IDENTITY(1,1), name VARCHAR(255), arrondissement INT, date_update DATETIME)")
        cursor.close()

    def get_data_from_api(self):
        # Récupération des données de l'API OpenData Paris
        url = "https://opendata.paris.fr/explore/dataset/velib-disponibilite-en-temps-reel/download/?format=json"&"timezone=Europe/Paris"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.station.stations = data
        else:
            raise Exception("Erreur lors de la récupération des données de l'API OpenData Paris")

    def save_data_to_database(self):
        # Insertion des données dans la base de données
        for station in self.station.stations:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO stations (name, arrondissement, date_update) VALUES (?, ?, ?)", (station["name"], station["arrondissement"], station["last_update"]))
            cursor.close()

    def get_station_la_plus_proche(self, adresse: str):
        return self.station.get_station_la_plus_proche(adresse)

    def get_station_la_moins_frequentee(self, date_debut, date_fin):
        # Récupération des données de la base de données
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM stations WHERE date_update BETWEEN ? AND ? ORDER BY available_bikes DESC", (date_debut, date_fin))
        data = cursor.fetchone()
        cursor.close()

        # Retour de la station la moins fréquentée
        return data[0] if data is not None else None

    def get_arrondissement_le_plus_frequente(self, date_debut, date_fin):
        # Récupération des données de la base de données
        cursor = self.connection.cursor()
        cursor.execute("SELECT arrondissement, COUNT(*) AS nb_usagers FROM stations WHERE date_update BETWEEN ? AND ? GROUP BY arrondissement ORDER BY nb_usagers DESC", (date_debut, date_fin))
        data = cursor.fetchone()
        cursor.close()

        # Retour de l'arrondissement le plus fréquenté
        return data[0] if data is not None else None
    
    @app.get("/stations")
    def get_stations():
        return self.station.get_stations()

    @app.get("/stations/closest")
    def get_closest_station(latitude: float, longitude: float):
        return self.station.get_closest_station(latitude, longitude)

    @app.get("/stations/least_frequented")
    def get_least_frequented_station(start_date: str, end_date: str):
        return self.station.get_least_frequented_station(start_date, end_date)

    @app.get("/stations/most_frequented_arrondissement")
    def get_most_frequented_arrondissement(start_date: str, end_date: str):
        return self.station.get_most_frequented_arrondissement(start_date, end_date)

if __name__ == "__main__":
    app.run(debug=True)

