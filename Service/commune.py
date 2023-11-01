

class Commune:
    def __init__(self, id_commune, nom_commune):
        self.id_commune = id_commune
        self.nom_commune = nom_commune

    def __repr__(self):
        return f"Commune(id={self.id_commune}, nom={self.nom_commune})"
