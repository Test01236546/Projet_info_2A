# from datetime import date


class jer_stationDAO:
    def __init__(self):
        self.stations = []

    def create(self, station):
        self.stations.append(station)
        print(f"Station créée : {station}")

    def read(self, id):
        for station in self.stations:
            if station.id == id:
                print(f"Station trouvée : {station}")
                return station
        print("Station non trouvée")
        return None

    def update(self, id, new_station):
        for i, station in enumerate(self.stations):
            if station.id == id:
                self.stations[i] = new_station
                print(f"Station mise à jour : {new_station}")
                return
        print("Station non trouvée")

    def delete(self, id):
        for i, station in enumerate(self.stations):
            if station.id == id:
                del self.stations[i]
                print(f"Station supprimée : {station}")
                return
        print("Station non trouvée")

    def insert(self, station):
        self.create(station)
