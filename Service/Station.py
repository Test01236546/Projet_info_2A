from pydantic import BaseModel

class Station(BaseModel):
    def __init__(self,id, nom_station, capacite, coordonnees_station, id_commune, en_fonctionnement, date_deb, date_fin, borne_paiement, nb_bornettes):
        """
        Initialise un objet Station pour effectuer différentes tâches.

        """
        
        self.id=id
        self.nom_station=nom_station
        self.capacite=capacite
        self.coordonnees_station=coordonnees_station
        self.id_commune=id_commune
        self.en_fonctionnement=en_fonctionnement
        self.date_deb=date_deb
        self.date_fin=date_fin
        self.borne_paiement=borne_paiement
        self.nb_bornettes=nb_bornettes

    def __str__(self):
        """
        Affiche toutes les informations relatives à une station.

        Returns:
            str: Informations d'une station Vélib'
        """
        return f"Station(id={self.id}, nom_station={self.nom_station}, capacite={self.capacite}, coordonnees_station ={self.coordonnees_station},id_commune={self.id_commune}, en_fonctionnement ={self.en_fonctionnement}, date_deb={self.date_deb}, date_fin={self.date_fin},borne_paiement={self.borne_paiement}, nb_bornettes={self.nb_bornettes})"


    

