class Service ():
    def __init__(self,id_stationfaits, id_station, id_temps):
        self.id_stationfaits=id_stationfaits
        self.id_station=id_station
        self.id_temps=id_temps

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
