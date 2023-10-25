class Station():
    def __init__(self,id, nom_station, capacite, coordonnes_station, nom_commune, en_fonctionnement, date_deb, date_fin, borne_paiement, nb_bornettes):
        self.id=id
        self.nom_station=nom_station
        self.capacite=capacite
        self.coordonnees_station=coordonnees_station
        self.nom_commune=nom_commune
        self.en_fonctionnement=en_fonctionnement
        self.date_deb=date_deb
        self.date_fin=date_fin
        self.borne_paiement=borne_paiement
        self.nb_bornettes=nb_bornettes

    def __str__(self):
        return f"Station(id={self.id}, nom_station={self.nom_station}, capacite={self.capacite}, ...)"


    

