
class StationFaits():
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

    def __str__(self):
        return (f"StationFaits(id={self.id_station}, nb_bornettes={self.nb_bornettes}, velos_dispos={self.velos_dispos},meca_dispo={self.meca_dispo}, elec_dispo={self.elec_dispo}, retour_velo={self.retour_velo}, frequence={self.frequence}, date_fait_deb={self.date_fait_deb}, date_fait_fin={self.date_fait_fin})")
