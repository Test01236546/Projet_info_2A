
class StationFaits():
    """"
    Crée la classe StationFaits
    """
    def __init__(self, id_station, nb_bornettes, velos_dispos, meca_dispo, elec_dispo, retour_velo, frequence, date_fait_deb, date_fait_fin ):
        self.id_station=id_station
        self.nb_bornettes=nb_bornettes
        self.velos_dispos=velos_dispos
        self.meca_dispo=meca_dispo
        self.elec_dispo=elec_dispo
        self.retour_velo=retour_velo
        self.frequence=frequence
        self.date_fait_deb=date_fait_deb
        self.date_fait_fin=date_fait_fin

    def calcul_frequence(self,former_StationFaits : StationFaits):
        return round(abs(self.meca_dispo+self.elec_dispo-(former_StationFaits.meca_dispo + former_StationFaits.elec_dispo)))



    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères de l'objet StationFaits.

        Returns:
            str: Une chaîne de caractères représentant l'objet StationFaits.
        """
        return (f"StationFaits(id={self.id_station}, nb_bornettes={self.nb_bornettes}, velos_dispos={self.velos_dispos},meca_dispo={self.meca_dispo}, elec_dispo={self.elec_dispo}, retour_velo={self.retour_velo}, frequence={self.frequence}, date_fait_deb={self.date_fait_deb}, date_fait_fin={self.date_fait_fin})")
