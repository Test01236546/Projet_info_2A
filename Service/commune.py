

class Commune:
    """
    Crée la classe Commune
    """
    def __init__(self, id_commune, nom_commune):
        """
        Initialise un objet Commune avec un identifiant et un nom de commune.

        Args:
            id_commune (str): L'identifiant de la commune.
            nom_commune (str): Le nom de la commune.
        """
        self.id_commune = id_commune
        self.nom_commune = nom_commune

    def __repr__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères de l'objet Commune.

        Returns:
            str: Une chaîne de caractères représentant l'objet Commune.
        """
        return f"Commune(id={self.id_commune}, nom={self.nom_commune})"
