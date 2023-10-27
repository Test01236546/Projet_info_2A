from TempsDAO import TempsDAO
from datetime import datetime

class Temps(TempsDAO):
    def __init__(self):
        pass

    def str_to_timestamp(duedate, date_format="%Y-%m-%dT%H:%M:%S+00:00"):
        try:
            timestamp = datetime.strptime(duedate, date_format).timestamp()
            return timestamp
        except ValueError:
            print("Erreur : Format de date/heure invalide")
        return None