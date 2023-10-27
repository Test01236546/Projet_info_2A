from jer_station_DAO import jer_stationDAO
from jer_station import jer_station


if __name__ == "__main__":
    
    StationDAO_Jer= jer_stationDAO()
    Station_Jer = jer_station("station.id_1", "station.nom_station", "station.capacite", "station.coordonnees_station", 
                "station.nom_commune", "station.en_fonctionnement", "station.date_deb", "station.date_fin", 
                "station.borne_paiement", "station.nb_bornettes")
    StationDAO_Jer.read("station.id_1")
    StationDAO_Jer.read("station.id")
    StationDAO_Jer.create(Station_Jer)
    StationDAO_Jer.read("station.id_1")
    Station_Jer_UPDATED = jer_station("station.id_1", "station.nom_station_UPDATED", "station.capacite_UPDATED", "station.coordonnees_station_UPDATED", 
                "station.nom_commune_UPDATED", "station.en_fonctionnement_UPDATED", "station.date_deb_UPDATED", "station.date_fin_UPDATED", 
                "station.borne_paiement_UPDATED", "station.nb_bornettes_UPDATED")
    StationDAO_Jer.update("station.id_1",Station_Jer_UPDATED)
    StationDAO_Jer.read("station.id_1")
