from AbstractDAO import DAO

class StationFaitsDAO(AbstractDAO):
    def __init__(self, id, id_temps, id_temps_fin, velos_dispo, meca_dispo, elec_dispo, retour_dispo):
        seld.id=id
        self.id_temps=id_temps
        self.id_temps_fin=id_temps_fin
        self.velos_dispo=velos_dispo
        self.meca_dispo=meca_dispo
        self.elec_dispo=elec_dispo
        self.retour_dispo=retour_dispo
        
    