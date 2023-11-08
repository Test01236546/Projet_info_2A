

class Temps:
    """
    Crée la classe Temps
    """
    def __init__(self, id_temps, date, annee, mois, jour, heure, minute):
        self.id_temps = id_temps
        self.date = date
        self.annee = annee
        self.mois = mois
        self.jour = jour
        self.heure = heure
        self.minute = minute

    def __repr__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères de l'objet Temps.

        Returns:
            str: Une chaîne de caractères représentant l'objet Temps.
        """
        return (f"Temps(id_temps={self.id_temps}, date={self.date}, annee={self.annee}, mois={self.mois},jour={self.jour}, heure={self.heure}, minute={self.minute})")
