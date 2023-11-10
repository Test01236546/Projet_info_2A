import sqlite3
import Service.StationFaits as stf

class StationFaitsDAO:
    """
    Crée la classe StationFaitsDAO qui permet de mettre à jour la table StationFaits dans la base de données
    """
    TABLE_NAME = "StationFaits"

    def __init__(self, db_path):
        """
        Initialise un objet d'accès aux données (DAO) pour la table 'StationFaits' dans une base de données SQLite.

        Args:
            db_path (str): Le chemin du fichier de base de données SQLite.
        """
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create(self, station_faits):
        """
        Crée un enregistrement de faits de station dans la base de données.

        Args:
            station_faits (StationFaits): L'objet StationFaits à insérer dans la base de données.
        """
        self.cur.execute(f"""
        INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (station_faits.id_station, station_faits.nb_bornettes, station_faits.velos_dispos, 
              station_faits.meca_dispo, station_faits.elec_dispo, station_faits.retour_velo, 
              station_faits.frequence, station_faits.date_fait_deb, station_faits.date_fait_fin))
        self.conn.commit()
        print("StationFaits créé")

    def create2(self,dict):         #on pourrait prendre deux liste (nom attributs de StationFaits, nom clées du dict station et matcher)
        StationFaits_to_add=stf.StationFaits(dict['stationcode'],dict['capacity'],dict['numbikesavailable'],dict['mechanical'],dict['ebike'],dict['is_returning'],f"frequence {dict['stationcode']}",dict['duedate'],f"date_fait_deb {dict['stationcode']}")
        self.cur.execute(f"""
        INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (StationFaits_to_add.id_station, StationFaits_to_add.nb_bornettes, StationFaits_to_add.velos_dispos, 
              StationFaits_to_add.meca_dispo, StationFaits_to_add.elec_dispo, StationFaits_to_add.retour_velo, 
              StationFaits_to_add.frequence, StationFaits_to_add.date_fait_deb, StationFaits_to_add.date_fait_fin))
        self.conn.commit()

    def read(self, id_station):
        """
        Recherche des faits de station dans la base de données en fonction de l'identifiant de la station.

        Args:
            id_station (str): L'identifiant de la station dont les faits doivent être recherchés.

        Returns:
            tuple or None: Un tuple contenant les données des faits de station (id_station, nb_bornettes, velos_dispos, meca_dispo, elec_dispo, retour_velo, frequence, date_fait_deb, date_fait_fin) ou None si les faits n'ont pas été trouvés.
        """
        self.cur.execute(f"SELECT * FROM {self.TABLE_NAME} WHERE id_station=?", (id_station,))
        station_faits_data = self.cur.fetchone()
        if station_faits_data:
            print("StationFaits trouvé:", station_faits_data)
            return station_faits_data
        else:
            print("StationFaits non trouvé")
            return None

    def update(self, id_station, new_data):
        """
        Met à jour les informations des faits de station dans la base de données.

        Args:
            id_station (str): L'identifiant de la station dont les faits doivent être mis à jour.
            new_data (StationFaits): L'objet StationFaits contenant les nouvelles données.

        Note:
            Cette méthode met à jour toutes les colonnes de la table StationFaits en fonction des données fournies.
        """
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET nb_bornettes=?, velos_dispos=?, meca_dispo=?, elec_dispo=?, 
        retour_velo=?, frequence=?, date_fait_deb=?, date_fait_fin=? WHERE id_station=?
        """, (new_data.nb_bornettes, new_data.velos_dispos, new_data.meca_dispo, new_data.elec_dispo, 
              new_data.retour_velo, new_data.frequence, new_data.date_fait_deb, 
              new_data.date_fait_fin, id_station))
        self.conn.commit()
        print("StationFaits mis à jour")

    def update2(self, dictionnaire):
        """
        Met à jour les informations des faits de station dans la base de données en utilisant les données fournies dans un dictionnaire.

        Args:
            dictionnaire (dict): Un dictionnaire contenant les nouvelles données des faits de station.
        """
        # Création d'une instance de StationFaits avec les données mises à jour
        StationFaits_to_update = stf.StationFaits(
            dictionnaire['stationcode'],
            dictionnaire['capacity'],
            dictionnaire['numbikesavailable'],
            dictionnaire['mechanical'],
            dictionnaire['ebike'],
            dictionnaire['is_returning'],
            f"frequence {dictionnaire['stationcode']}",
            dictionnaire['duedate'],
            f"date_fait_deb {dictionnaire['stationcode']}"
        )

        # Mise à jour de l'enregistrement dans la base de données
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET nb_bornettes=?, velos_dispos=?, meca_dispo=?, elec_dispo=?, 
        retour_velo=?, frequence=?, date_fait_deb=?, date_fait_fin=? WHERE id_station=?
        """, (
            StationFaits_to_update.nb_bornettes,
            StationFaits_to_update.velos_dispos,
            StationFaits_to_update.meca_dispo,
            StationFaits_to_update.elec_dispo,
            StationFaits_to_update.retour_velo,
            StationFaits_to_update.frequence,
            StationFaits_to_update.date_fait_deb,
            StationFaits_to_update.date_fait_fin,
            StationFaits_to_update.id_station
        ))
        self.conn.commit()
        print(f"StationFaits pour la station {StationFaits_to_update.id_station} mis à jour")

    def delete(self, id_station):
        """
        Supprime les faits de station de la base de données en fonction de l'identifiant de la station.

        Args:
            id_station (str): L'identifiant de la station dont les faits doivent être supprimés.
        """
        self.cur.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id_station=?", (id_station,))
        self.conn.commit()
        print("StationFaits supprimé")

    def close(self):
        """
        Ferme la connexion à la base de données.
        """

        self.conn.close()

    def upsert2(self, dictionnaire):

        # Construction de la requête pour vérifier l'existence de l'élément
        self.cur.execute("SELECT * FROM StationFaits WHERE id_station=?", (dict['stationcode'],))
        existing_record = self.cur.fetchone()

        if existing_record:
            # Si l'enregistrement existe, créer une instance de StationFaits avec les données existantes
            former_StationFaits = stf.StationFaits(*existing_record)

                # Création d'une instance de StationFaits
            StationFaits_to_upsert = stf.StationFaits(
                dictionnaire['stationcode'],
                dictionnaire['capacity'],
                dictionnaire['numbikesavailable'],
                dictionnaire['mechanical'],
                dictionnaire['ebike'],
                dictionnaire['is_returning'],
                "frequence pas encore update",
                dictionnaire['duedate'],
                f"date_fait_fin {dictionnaire['stationcode']}"
            )



            # Tentative de mise à jour
            self.cur.execute(f"""
            UPDATE {self.TABLE_NAME} SET nb_bornettes=?, velos_dispos=?, meca_dispo=?, elec_dispo=?,
            retour_velo=?, frequence=?, date_fait_deb=?, date_fait_fin=? WHERE id_station=?
            """, (
                StationFaits_to_upsert.nb_bornettes,
                StationFaits_to_upsert.velos_dispos,
                StationFaits_to_upsert.meca_dispo,
                StationFaits_to_upsert.elec_dispo,
                StationFaits_to_upsert.retour_velo,
                StationFaits_to_upsert.calcul_frequence(former_StationFaits),
                StationFaits_to_upsert.date_fait_deb,
                StationFaits_to_upsert.date_fait_fin,
                StationFaits_to_upsert.id_station
            ))
            
        else : 
            self.cur.execute(f"""
            INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                StationFaits_to_upsert.id_station,
                StationFaits_to_upsert.nb_bornettes,
                StationFaits_to_upsert.velos_dispos,
                StationFaits_to_upsert.meca_dispo,
                StationFaits_to_upsert.elec_dispo,
                StationFaits_to_upsert.retour_velo,
                0,
                StationFaits_to_upsert.date_fait_deb,
                StationFaits_to_upsert.date_fait_fin
            ))

        self.conn.commit()
        print(f"StationFaits pour la station {StationFaits_to_upsert.id_station} mise à jour ou insérée")
