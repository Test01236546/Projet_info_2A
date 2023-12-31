from pydantic import BaseModel
from datetime import datetime

class Station(BaseModel):
    id: str
    nom_station: str
    capacite: int
    coordonnees_station: str
    id_commune: str
    en_fonctionnement: str
    date_deb: datetime
    date_fin: datetime
    borne_paiement: str
    nb_bornettes: int
    # def __init__(self,id, nom_station, capacite, coordonnees_station, id_commune, en_fonctionnement, date_deb, date_fin, borne_paiement, nb_bornettes):
    #     """
    #     Initialise un objet Station pour effectuer différentes tâches.

    #     """
        
    #     self.id=id
    #     self.nom_station=nom_station
    #     self.capacite=capacite
    #     self.coordonnees_station=coordonnees_station
    #     self.id_commune=id_commune
    #     self.en_fonctionnement=en_fonctionnement
    #     self.date_deb=date_deb
    #     self.date_fin=date_fin
    #     self.borne_paiement=borne_paiement
    #     self.nb_bornettes=nb_bornettes

    def __str__(self):
        """
        Affiche toutes les informations relatives à une station.

        Returns:
            str: Informations d'une station Vélib'
        """
        return f"Station(id={self.id}, nom_station={self.nom_station}, capacite={self.capacite}, coordonnees_station ={self.coordonnees_station},id_commune={self.id_commune}, en_fonctionnement ={self.en_fonctionnement}, date_deb={self.date_deb}, date_fin={self.date_fin},borne_paiement={self.borne_paiement}, nb_bornettes={self.nb_bornettes})"


    
#{'stationcode': '16107', 
# 'name': 'Benjamin Godard - Victor Hugo',
#  'is_installed': 'OUI', 'capacity': 35,
#  'numdocksavailable': 34,
#  'numbikesavailable': 1,
#  'mechanical': 1,
#  'ebike': 0,
#  'is_renting': 'OUI',
#  'is_returning': 'OUI',
#  'duedate': '2023-12-12T01:48:43+01:00',
#  'coordonnees_geo': {'lon': 2.275725, 'lat': 48.865983},
#  'nom_arrondissement_communes': 'Paris',
#  'code_insee_commune': None}
