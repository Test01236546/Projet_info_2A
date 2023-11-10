
import sqlite3
import Service.Temps as tp
from datetime import datetime

class TempsDAO:
    """
    Crée la classe TempsDAO qui permet de mettre à jour la table Temps dans la base de données
    """
    TABLE_NAME = "Temps"

    def __init__(self, db_path):
        """
        Initialise un objet d'accès aux données (DAO) pour la table 'Temps' dans une base de données SQLite.

        Args:
            db_path (str): Le chemin du fichier de base de données SQLite.
        """
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create(self, temps):
        """
        Crée un enregistrement de temps dans la base de données.

        Args:
            temps (Temps): L'objet Temps à insérer dans la base de données.
        """
        self.cur.execute(f"""
        INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (temps.id_temps, temps.date, temps.annee, temps.mois, temps.jour, temps.heure, temps.minute))
        self.conn.commit()
        print("Temps créé")

    def create2(self,dict):
        date_string = dict['duedate']
        timestamp = datetime.fromisoformat(date_string)

        year = timestamp.year
        month = timestamp.month
        day = timestamp.day
        hour = timestamp.hour
        minute = timestamp.minute

        Temps_to_add = tp.Temps(dict['stationcode'],timestamp,year,month,day,hour,minute)

        self.cur.execute(f"""
        INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (Temps_to_add.id_temps, Temps_to_add.date, Temps_to_add.annee, Temps_to_add.mois, Temps_to_add.jour, Temps_to_add.heure, Temps_to_add.minute))
        self.conn.commit()


        

    def read(self, id_temps):
        """
        Recherche un enregistrement de temps dans la base de données en fonction de son identifiant.

        Args:
            id_temps (str): L'identifiant du temps à rechercher.

        Returns:
            tuple or None: Un tuple contenant les données de temps (id_temps, date, annee, mois, jour, heure, minute) ou None si le temps n'a pas été trouvé.
        """
        self.cur.execute(f"SELECT * FROM {self.TABLE_NAME} WHERE id_temps=?", (id_temps,))
        temps_data = self.cur.fetchone()
        if temps_data:
            print("Temps trouvé:", temps_data)
            return temps_data
        else:
            print("Temps non trouvé")
            return None

    def update(self, id_temps, new_data):
        """
        Met à jour les informations de temps dans la base de données.

        Args:
            id_temps (str): L'identifiant du temps à mettre à jour.
            new_data (Temps): L'objet Temps contenant les nouvelles données.
        """
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET date=?, annee=?, mois=?, jour=?, heure=?, minute=? WHERE id_temps=?
        """, (new_data.date, new_data.annee, new_data.mois, new_data.jour, new_data.heure, new_data.minute, id_temps))
        self.conn.commit()
        print("Temps mis à jour")


    def update2(self, dictionnaire):
        """
        Met à jour les informations de temps dans la base de données en utilisant les données fournies dans un dictionnaire.

        Args:
            dictionnaire (dict): Un dictionnaire contenant les nouvelles données de temps.
        """
        # Extraction de la date et de l'heure à partir de la chaîne ISO
        date_string = dictionnaire['duedate']
        timestamp = datetime.fromisoformat(date_string)

        year = timestamp.year
        month = timestamp.month
        day = timestamp.day
        hour = timestamp.hour
        minute = timestamp.minute

        # Création d'une instance de Temps avec les données mises à jour
        Temps_to_update = tp.Temps(
            dictionnaire['id_temps'],
            timestamp,
            year,
            month,
            day,
            hour,
            minute
        )

        # Mise à jour de l'enregistrement dans la base de données
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET date=?, annee=?, mois=?, jour=?, heure=?, minute=? WHERE id_temps=?
        """, (
            Temps_to_update.date,
            Temps_to_update.annee,
            Temps_to_update.mois,
            Temps_to_update.jour,
            Temps_to_update.heure,
            Temps_to_update.minute,
            Temps_to_update.id_temps
        ))
        self.conn.commit()
        print(f"Temps pour l'identifiant {Temps_to_update.id_temps} mis à jour")


    def delete(self, id_temps):
        """
        Supprime un enregistrement de temps de la base de données en fonction de son identifiant.

        Args:
            id_temps (str): L'identifiant du temps à supprimer.
        """
        self.cur.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id_temps=?", (id_temps,))
        self.conn.commit()
        print("Temps supprimé")

    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

    def upsert2(self, dictionnaire):
        # Traitement de la date
        date_string = dictionnaire['duedate']
        timestamp = datetime.fromisoformat(date_string)
        year = timestamp.year
        month = timestamp.month
        day = timestamp.day
        hour = timestamp.hour
        minute = timestamp.minute

        # Création d'une instance de Temps
        Temps_to_upsert = Temps(
            dictionnaire['stationcode'],
            timestamp,
            year,
            month,
            day,
            hour,
            minute
        )

        # Tentative de mise à jour
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET date=?, annee=?, mois=?, jour=?, heure=?, minute=? WHERE id_temps=?
        """, (
            Temps_to_upsert.date,
            Temps_to_upsert.annee,
            Temps_to_upsert.mois,
            Temps_to_upsert.jour,
            Temps_to_upsert.heure,
            Temps_to_upsert.minute,
            Temps_to_upsert.id_temps
        ))

        # Vérification et insertion si nécessaire
        if self.cur.rowcount == 0:
            self.cur.execute(f"""
            INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                Temps_to_upsert.id_temps,
                Temps_to_upsert.date,
                Temps_to_upsert.annee,
                Temps_to_upsert.mois,
                Temps_to_upsert.jour,
                Temps_to_upsert.heure,
                Temps_to_upsert.minute
            ))

        self.conn.commit()
        print(f"Temps pour l'identifiant {Temps_to_upsert.id_temps} mis à jour ou inséré")

