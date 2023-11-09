# from jer_stationDAO import Jer_stationDAO
# from jer_station import Jer_station
# import sys
# sys.path.append('BDD/classBDD.py')
# import time
import requests
import json

from Service import Station as st
from Service import commune as cm
from Service import Temps as tp
from Service import StationFaits as stf

from DAO import StationDAO as stDAO
from DAO import communeDAO as cmDAO
from DAO import TempsDAO as tpDAO
from DAO import StationFaitsDAO as stfDAO

from BDD import classBDD as cBDD



if __name__ == "__main__":
    BDD_PATH_TEST = "Test_Jeremie/test1.sql"
    db_manager = cBDD.BDD_Manager(BDD_PATH_TEST)
    # db_manager.create_stations_table() #pas besoin
    
    # #StationDAO
    # Instance_StationDAO = stDAO.StationDAO(BDD_PATH_TEST)
    # Instance_Station = st.Station("station.id_1", "station.nom_station", "station.capacite", "station.coordonnees_station", 
    #            "station.nom_commune", "station.en_fonctionnement", "station.date_deb", "station.date_fin", 
    #            "station.borne_paiement","nb_bornettes")
    # # Instance_StationDAO.read("station.id")
    # Instance_StationDAO.delete("station.id_1")
    # Instance_StationDAO.create(Instance_Station)
    # Instance_StationDAO.read("station.id_1")
    # Instance_Station_UPDATE = st.Station("station.id_1", "station.nom_station_UPDATE", "station.capacite", "station.coordonnees_station", 
    #            "station.nom_commune", "station.en_fonctionnement", "station.date_deb", "station.date_fin", 
    #            "station.borne_paiement", "station.nb_bornettes")
    # Instance_StationDAO.update("station.id_1",Instance_Station_UPDATE)
    # Instance_StationDAO.read("station.id_1")
    # Instance_StationDAO.cur.execute("PRAGMA table_info(Station)")
    # result = Instance_StationDAO.cur.execute("PRAGMA table_info(Station)").fetchall() # visionner les colonnes de la table
    # print(result)
    # for row in result:
    #     print(row)
    
    # #CommuneDAO
    # Instance_CommuneDAO = cmDAO.CommuneDAO(BDD_PATH_TEST)
    # Instance_Commune = cm.Commune(97232,"Lamentin")
    # Instance_CommuneDAO.read(97232)
    # Instance_CommuneDAO.create(Instance_Commune)
    # Instance_CommuneDAO.delete(97232)
    # Instance_Commune_UPDATED = cm.Commune(97232,"Lamentin_UPDATED") 
    # Instance_CommuneDAO.update(97232,Instance_Commune_UPDATED)
    
    # #TempsDAO
    # Instance_TempsDAO = tpDAO.TempsDAO(BDD_PATH_TEST)
    # Instance_Temps = tp.Temps("id_temps_1", "date_1", "annee_1", "mois_1", "jour_1", "heure_1", "minute_1")
    # Instance_TempsDAO.read("id_temps_1")
    # Instance_TempsDAO.create(Instance_Temps)
    # Instance_TempsDAO.delete("id_temps_1")
    # Instance_Temps_UPDATED = tp.Temps("id_temps_1", "date_1_UPDATED", "annee_1_UPDATED", "mois_1_UPDATED", "jour_1_UPDATED", "heure_1_UPDATED", "minute_1_UPDATED")
    # Instance_TempsDAO.update("id_temps_1",Instance_Temps_UPDATED)

    # #StationFaitsDAO
    # Instance_StationFaitsDAO = stfDAO.StationFaitsDAO(BDD_PATH_TEST)
    # Instance_StationFait = stf.StationFaits("id", "nb_bornettes", "velos_dispos", 
    #           "meca_dispo", "elec_dispo", "retour_velo", 
    #           "frequence", "date_fait_deb", "date_fait_fin")
    # Instance_StationFaitsDAO.read("id")
    # Instance_StationFaitsDAO.create(Instance_StationFait)
    # Instance_StationFaitsDAO.delete("id")
    # Instance_StationFait_UPDATED = stf.StationFaits("id", "nb_bornettes_UP", "velos_dispos_UP", 
    #           "meca_dispo_UP", "elec_dispo_UP", "retour_velo_UP", 
    #           "frequence_UP", "date_fait_deb_UP", "date_fait_fin_UP")
    # Instance_StationFaitsDAO.update("id",Instance_StationFait_UPDATED)


    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"
    response = requests.get(url)
    data = response.json()
    # cles = list(data.keys())
    # print(cles)

    results = data['results']
    # type(results)
    # results[54]
    # cles_results = list(results.keys()) 
    # print(cles_results)       



    # Ouvrir les bases de données
    Instance_StationDAO = stDAO.StationDAO(BDD_PATH_TEST)
    # Instance_CommuneDAO = cmDAO.CommuneDAO(BDD_PATH_TEST)
    # Instance_TempsDAO = tpDAO.TempsDAO(BDD_PATH_TEST)
    # Instance_StationFaitsDAO = stfDAO.StationFaitsDAO(BDD_PATH_TEST)


    #data a deux clés (total et results), results est une liste de dictionnaires dons les keys-values sont des infos sur la station
    #ON VA VECTORISER LES CLACULS AVEC UN APPLY, on fait un create2 qui créé directement la station(resp le reste) puis la met dans la table
    # list(map(lambda station_dict: Instance_StationDAO.create2(station_dict), data['results']))
    # list(map(lambda station_dict: Instance_CommuneDAO.create2(station_dict), data['results']))
    # list(map(lambda station_dict: Instance_TempsDAO.create2(station_dict), data['results']))
    # list(map(lambda station_dict: Instance_StationFaitsDAO.create2(station_dict), data['results']))

    dict_statio_test = results[0]
    # dict_statio_test['stationcode']
    # Instance_Station
    # json.dumps(dict_statio_test['coordonnees_geo'])
    Instance_StationDAO.create2(dict_statio_test)
    dict_statio_test
    dict_statio_test['stationcode']
    Instance_StationDAO.read('19033')
    
    #test
    list(map(lambda station_dict: Instance_StationDAO.create2(station_dict), data['results']))

    # Verifier_Station_create2 = Instance_StationDAO.create2(dict_statio_test)

    # print(Verifier_Station_create2)
    # Verifier_Station_create2.nom_station

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








        