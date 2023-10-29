from DAO.StationFaitsDAO import StationFaitsDAO

class StationFaits():
    def __init__(self, id, id_temps, velos_dispos, meca_dispo, elec_dispo, retour_velo ):
        self.id=id
        self.id_temps=id_temps
        self.velos_dispos=velos_dispos
        self.meca_dispo=meca_dispo
        self.elec_dispo=elec_dispo
        self.retour_velo=retour_velo
