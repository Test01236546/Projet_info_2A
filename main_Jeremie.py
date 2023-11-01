# from jer_stationDAO import Jer_stationDAO
# from jer_station import Jer_station
# import sys
# sys.path.append('BDD/classBDD.py')
# import time
from Service import station as St
from DAO import stationDAO as stDAO
from BDD import classBDD as cBDD


if __name__ == "__main__":
    BDD_PATH = "Test_Jeremie/test1.sql"
    db_manager = cBDD.BDD_Manager(BDD_PATH)
    # db_manager.create_stations_table() #pas besoin
    Instance_StationDAO = stDAO.StationDAO(BDD_PATH)
    Instance_Station = St.Station("station.id_1", "station.nom_station", "station.capacite", "station.coordonnees_station", 
               "station.nom_commune", "station.en_fonctionnement", "station.date_deb", "station.date_fin", 
               "station.borne_paiement", "station.nb_bornettes")
    # Instance_StationDAO.read("station.id")
    Instance_StationDAO.delete("station.id_1")
    Instance_StationDAO.create(Instance_Station)
    Instance_StationDAO.read("station.id_1")
    Instance_Station_UPDATE = St.Station("station.id_1", "station.nom_station_UPDATE", "station.capacite", "station.coordonnees_station", 
               "station.nom_commune", "station.en_fonctionnement", "station.date_deb", "station.date_fin", 
               "station.borne_paiement", "station.nb_bornettes")
    Instance_StationDAO.update1("station.id_1",Instance_Station_UPDATE)
    Instance_StationDAO.update2("station.id_1",Instance_Station_UPDATE)
    Instance_StationDAO.read("station.id_1")
    Instance_StationDAO.cur.execute("PRAGMA table_info(Station)")
    result = Instance_StationDAO.cur.execute("PRAGMA table_info(Station)").fetchall()
    print(result)
    for row in result:
        print(row)




#TEST LOCAUX    
#    StationDAO_Jer= Jer_stationDAO()
#    Station_Jer = jer_station("station.id_1", "station.nom_station", "station.capacite", "station.coordonnees_station", 
#                "station.nom_commune", "station.en_fonctionnement", "station.date_deb", "station.date_fin", 
#                "station.borne_paiement", "station.nb_bornettes")
#    StationDAO_Jer.read("station.id_1")
#    StationDAO_Jer.read("station.id")
#    StationDAO_Jer.create(Station_Jer)
#    StationDAO_Jer.read("station.id_1")
#    Station_Jer_UPDATED = jer_station("station.id_1", "station.nom_station_UPDATED", "station.capacite_UPDATED", "station.coordonnees_station_UPDATED", 
#                "station.nom_commune_UPDATED", "station.en_fonctionnement_UPDATED", "station.date_deb_UPDATED", "station.date_fin_UPDATED", 
#                "station.borne_paiement_UPDATED", "station.nb_bornettes_UPDATED")
#    StationDAO_Jer.update("station.id_1",Station_Jer_UPDATED)
#    StationDAO_Jer.read("station.id_1")

#TEST GLOBAUX




# if __name__ == "__main__":
#     while True:
#         BDD.classBDD.BDD_Manager.create_stations_table()
#         # Mettre à jour les bases de données
#         ingest()
#         # Attendre 1 minute avant de se mettre à jour à nouveau
#         time.sleep(60)








        