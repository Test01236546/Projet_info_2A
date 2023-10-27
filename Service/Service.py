import requests
import pyodbc
from datetime import datetime

class Service ():
    def __init__(self,id_stationfaits, id_station, id_temps):
        self.id_stationfaits=id_stationfaits
        self.id_station=id_station
        self.id_temps=id_temps
        self.connection = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=velib;UID=sa;PWD=password")

    def ingest(self):
        # Récupération des données de l'API
        url = "https://opendata.paris.fr/explore/dataset/velib-disponibilite-en-temps-reel/download/?format=json"&"timezone=Europe/Paris"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            raise Exception("Erreur lors de la récupération des données de l'API OpenData Paris")

        # Récupération de la date de la dernière mise à jour de la base de données
        cursor = self.connection.cursor()
        cursor.execute("SELECT MAX(date_update) AS date_update FROM stations")
        last_update = cursor.fetchone()[0]
        cursor.close()

        # Insertion des nouvelles données dans la base de données
        for station in data:
            # Vérification que la station n'est pas déjà présente dans la base de données
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(*) AS nb FROM stations WHERE name = ?", (station["name"],))
            count = cursor.fetchone()[0]
            cursor.close()

            # Insertion de la nouvelle station dans la base de données si elle n'y est pas encore
            if count == 0:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO stations (name, arrondissement, date_update) VALUES (?, ?, ?)", (station["name"], station["arrondissement"], datetime.utcfromtimestamp(station["last_update"])))
                cursor.close()

            # Mise à jour de la date de mise à jour de la station si elle est déjà présente dans la base de données
            else:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE stations SET date_update = ? WHERE name = ?", (datetime.utcfromtimestamp(station["last_update"]), station["name"]))
                cursor.close()

        # Fermeture de la connexion à la base de données
        self.connection.close()


if __name__ == "__main__":
    service = Service()
    service.ingest()